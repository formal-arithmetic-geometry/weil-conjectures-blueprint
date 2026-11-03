// comments.js — the comment section at the foot of an object page and of
// every page of the document, kept on the project's Zulip.
//
// This file replaces the blueprint tool's web/comments.js on the deployed site
// (the step "Keep the comments on Zulip" of .github/workflows/site.yml).  The
// tool's version talks to the comment server of `blueprint serve`, which the
// static hosting on fuxi does not run; this one talks to Zulip straight from
// the browser, which the Zulip server allows (CORS with an Authorization
// header).  It exports what the tool's pages import: `commentsPanel` and
// `DOCUMENT_THREAD`.
//
// Every comment is a message of the comment bot in the channel of
// comments-config.json, in the topic of its object (`topicOf`).  Its first line
// says who wrote it and whether it is public or private; the page shows the
// bot's public messages of the topic, so a message edited or deleted on Zulip
// is a comment edited or deleted here.  Private comments are only on Zulip.
//
// comments-config.json is written next to index.html by the workflow, with
// the bot's key from the repository's secrets:
//   {"zulip": {"site": "https://…", "channel": "…", "email": "…", "key": "…"}}
// Without it the section says that comments are not set up.

/** The thread of the top page of the document, as in the tool's comments.js. */
export const DOCUMENT_THREAD = ':document';

const NAME_KEY = 'blueprint.commentName';
const VISIBILITY_KEY = 'blueprint.commentVisibility';
const MAX_TOPIC = 60; // Zulip's default limit on the length of a topic
const MAX_NAME = 100;
const MAX_BODY = 9000; // Zulip's limit is 10000 for the whole message

const MARKS = { public: '🌐 **Public**', private: '🔒 **Private**' };
const HEAD_RE = /^(?:🌐|🔒) \*\*(Public|Private)\*\* comment by \*\*([^*\n]*)\*\* on [^\n]*\n*/u;

let panels = 0; // for the names of each panel's radio buttons

function remembered(key) {
  try { return localStorage.getItem(key) || ''; } catch (e) { return ''; }
}

function remember(key, value) {
  try { localStorage.setItem(key, value); } catch (e) { /* private mode */ }
}

let configPromise = null;

/** comments-config.json, or null when the site has none (asked again next time). */
function loadConfig() {
  if (!configPromise) {
    configPromise = fetch('comments-config.json', { cache: 'no-store' })
      .then((res) => (res.ok ? res.json() : null))
      .then((c) => {
        const z = c && c.zulip;
        return z && z.site && z.channel && z.email && z.key ? z : null;
      })
      .catch(() => null)
      .then((z) => {
        if (!z) configPromise = null;
        return z;
      });
  }
  return configPromise;
}

/** FNV-1a, as eight hex digits: tells apart ids cut to the same topic. */
function hash8(s) {
  let h = 0x811c9dc5;
  for (const b of new TextEncoder().encode(s)) {
    h ^= b;
    h = Math.imul(h, 0x01000193) >>> 0;
  }
  return h.toString(16).padStart(8, '0');
}

/** The Zulip topic of an object's comments: its id, cut to fit with a hash. */
export function topicOf(id) {
  const t = id === DOCUMENT_THREAD ? 'document (top page)' : id;
  const chars = [...t];
  if (chars.length <= MAX_TOPIC) return t;
  return chars.slice(0, MAX_TOPIC - 10).join('') + '… ' + hash8(t);
}

/** Zulip's encoding of one part of a `#narrow/…` link. */
function narrowPart(s) {
  return encodeURIComponent(s)
    .replace(/[!'()*.]/g, (c) => '%' + c.charCodeAt(0).toString(16).toUpperCase())
    .replace(/%/g, '.');
}

/** The first line of a comment's message, which `parseMessage` reads back. */
function headLine(visibility, name, title, url) {
  const label = title.replace(/[[\]\\]/g, (c) => '\\' + c);
  return `${MARKS[visibility]} comment by **${name}** on [${label}](${url})`;
}

/** {visibility, name, body} of a message the bot posted for a comment, or null. */
export function parseMessage(content) {
  const m = HEAD_RE.exec(content);
  if (!m) return null;
  return { visibility: m[1].toLowerCase(), name: m[2], body: content.slice(m[0].length) };
}

async function zulip(z, method, path, params) {
  const url = new URL('api/v1/' + path, z.site.replace(/\/*$/, '/'));
  const query = new URLSearchParams(params);
  // Only the Authorization header, which the server's CORS rules admit; the
  // form body is a content type that needs no permission of its own.
  const init = { method, headers: { Authorization: 'Basic ' + btoa(z.email + ':' + z.key) }, cache: 'no-store' };
  if (method === 'GET') url.search = query.toString();
  else init.body = query;
  const res = await fetch(url, init);
  const data = await res.json().catch(() => ({}));
  if (!res.ok || data.result !== 'success') throw new Error(data.msg || 'HTTP ' + res.status);
  return data;
}

export function commentsPanel(app, id) {
  const { el, clear } = app;
  const topic = topicOf(id);
  const heading = el('h3', 'Comments');
  const list = el('div.comment-list', el('p.muted.small', 'Loading comments…'));

  // ---- the form: name, public or private, Markdown + LaTeX, a preview, post
  const name = el('input', {
    type: 'text', name: 'name', required: true, maxlength: String(MAX_NAME), autocomplete: 'name',
    placeholder: 'Your name', 'aria-label': 'Name',
  });
  name.value = remembered(NAME_KEY);
  const group = 'comment-visibility-' + ++panels;
  const radio = (value) => el('input', { type: 'radio', name: group, value });
  const isPublic = radio('public');
  const isPrivate = radio('private');
  (remembered(VISIBILITY_KEY) === 'private' ? isPrivate : isPublic).checked = true;
  const text = el('textarea', {
    name: 'body', required: true, rows: '7', maxlength: String(MAX_BODY),
    placeholder: 'Markdown and LaTeX: $\\pi$, $$\\int_X f$$, and [label] to refer to an object.',
    'aria-label': 'Comment',
  });
  const preview = el('div.comment-preview.body-prose', { hidden: true });
  const previewBtn = el('button', { type: 'button', 'aria-pressed': 'false' }, 'Preview');
  const post = el('button.primary', { type: 'submit' }, 'Post comment');
  const note = el('span.comment-note.muted.small');
  const where = el('span');
  const form = el('form.comment-form',
    el('h4', 'Add a comment'),
    el('label.comment-field', el('span', 'Name'), name),
    el('div.comment-field', { role: 'radiogroup', 'aria-label': 'Who sees it' },
      el('span', 'Who sees it'),
      el('label', isPublic, ' Public: shown below this page and posted to Zulip'),
      el('label', isPrivate, ' Private: posted to Zulip only')),
    el('label.comment-field', el('span', 'Comment'), text),
    preview,
    el('p.muted.small', 'You can use Markdown and LaTeX style mathematics; ',
      el('code', '[label]'), ' links to the object with that label. ', where),
    el('div.row', previewBtn, post, note));

  const showPreview = (on) => {
    preview.hidden = !on;
    text.hidden = on;
    previewBtn.textContent = on ? 'Edit' : 'Preview';
    previewBtn.setAttribute('aria-pressed', on ? 'true' : 'false');
    if (on) {
      app.renderBody(preview, text.value.trim() ? text.value : '*Nothing to preview yet.*',
        app.knownIds(), undefined, { untrusted: true });
    }
  };
  previewBtn.addEventListener('click', () => showPreview(preview.hidden));

  const draw = (comments) => {
    clear(list);
    heading.textContent = `Comments (${comments.length})`;
    if (!comments.length) {
      list.appendChild(el('p.muted.small', 'No public comments yet.'));
      return;
    }
    for (const c of comments) {
      const body = el('div.comment-body.body-prose');
      app.renderBody(body, c.body, app.knownIds(), undefined, { untrusted: true });
      const when = new Date(c.date);
      list.appendChild(el('article.comment', { id: 'comment-' + c.n },
        el('div.comment-head',
          el('b', c.name),
          Number.isNaN(when.getTime()) ? null
            : el('time.muted.small', { datetime: c.date }, when.toLocaleString()),
          el('span.muted.small.comment-anchor', '#' + c.n)),
        body));
    }
  };

  const say = (target, ...parts) => {
    clear(target);
    for (const p of parts) target.append(p);
  };

  const unavailable = () => {
    clear(list);
    heading.textContent = 'Comments';
    list.appendChild(el('p.muted.small',
      'Comments are not set up on this copy of the site: it has no Zulip bot to post them with.'));
    clear(where);
    for (const c of [name, isPublic, isPrivate, text, previewBtn, post]) c.disabled = true;
  };

  let z = null;

  const load = async () => {
    z = await loadConfig();
    if (!z) return unavailable();
    const topicLink = (streamId) => el('a', {
      href: z.site.replace(/\/*$/, '') + '/#narrow/channel/'
        + narrowPart(streamId + '-' + z.channel) + '/topic/' + narrowPart(topic),
      target: '_blank', rel: 'noopener',
    }, `#${z.channel} › ${topic}`);
    say(where, 'Every comment is posted to Zulip, in ', el('b', `#${z.channel} › ${topic}`),
      '; public ones are also shown here.');
    try {
      const [stream, data] = await Promise.all([
        zulip(z, 'GET', 'get_stream_id', { stream: z.channel }),
        zulip(z, 'GET', 'messages', {
          anchor: 'newest', num_before: '1000', num_after: '0', apply_markdown: 'false',
          narrow: JSON.stringify([
            { operator: 'channel', operand: z.channel },
            { operator: 'topic', operand: topic },
            { operator: 'sender', operand: z.email },
          ]),
        }),
      ]);
      say(where, 'Every comment is posted to Zulip, in ', topicLink(stream.stream_id),
        '; public ones are also shown here.');
      const comments = [];
      for (const m of data.messages || []) {
        const c = parseMessage(String(m.content || ''));
        if (c && c.visibility === 'public') {
          comments.push({ n: m.id, name: c.name, body: c.body, date: new Date(m.timestamp * 1000).toISOString() });
        }
      }
      draw(comments);
    } catch (e) {
      clear(list);
      heading.textContent = 'Comments';
      list.appendChild(el('p.muted.small', `Could not read the comments from Zulip (${e.message}).`));
    }
  };

  form.addEventListener('submit', async (ev) => {
    ev.preventDefault();
    if (!z) return;
    const who = name.value.replace(/[*\r\n]+/g, ' ').trim();
    const what = text.value.trim();
    if (!who || !what) {
      note.textContent = 'A name and a comment, please.';
      return;
    }
    const visibility = isPrivate.checked ? 'private' : 'public';
    const o = app.model && app.model.byId ? app.model.byId.get(id) : null;
    const title = id === DOCUMENT_THREAD ? 'the document' : (o && o.attrs && o.attrs.title) || id;
    const page = location.href.split('#')[0]
      + (id === DOCUMENT_THREAD ? '#/document' : '#/object/' + encodeURIComponent(id));
    post.disabled = true;
    note.textContent = 'Posting…';
    try {
      await zulip(z, 'POST', 'messages', {
        type: 'stream', to: z.channel, topic,
        content: headLine(visibility, who, title, page) + '\n\n' + what,
      });
      remember(NAME_KEY, who);
      remember(VISIBILITY_KEY, visibility);
      text.value = '';
      showPreview(false);
      note.textContent = visibility === 'public' ? 'Posted.' : 'Posted to Zulip (private: not shown here).';
      if (visibility === 'public') await load();
    } catch (e) {
      note.textContent = 'Not posted: ' + e.message;
    } finally {
      post.disabled = false;
    }
  });

  load();
  return el('div.panel.comments', { id: 'comments' }, heading, list, form);
}
