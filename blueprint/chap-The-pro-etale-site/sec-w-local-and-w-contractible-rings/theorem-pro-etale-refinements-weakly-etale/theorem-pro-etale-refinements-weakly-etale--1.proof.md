+++
kind = "proof"
of = "theorem-pro-etale-refinements-weakly-etale--1"
order = 62002
uses = ["lemma-stability", "proposition-etale-implications", "proposition-w-local-components"]
+++
The w-strict localization $C$ is a faithfully flat ind-étale
$R$-algebra. It is constructed by w-localizing $R$, taking an
ind-étale contraction whose local rings at closed points are strictly
henselian, and w-localizing again along the extended ideal of closed
points. The ring $C$ is w-strictly local, and $V(J)$ is its set of
closed points.

By Lemma [lemma-stability], $C\to D'$ is weakly étale and $B\to D'$
is ind-étale. The latter map is also faithfully flat by base change.
Weakly étale maps induce algebraic residue field extensions: their
fibres are ind-étale over fields, so the residue extensions are
separable, hence algebraic. Consequently $V(K)$ consists of closed
points of $\operatorname{Spec}(D')$. The w-localization along $K$
gives an ind-Zariski map $D'\to D$, where $D$ is w-local and

$$
V(JD)=\operatorname{Spec}(D)^c.
$$

In particular, every maximal ideal $\mathfrak n$ of $D$ lies over a
maximal ideal $\mathfrak m$ of $C$. The map $C\to D$ is weakly
étale, using Proposition [proposition-etale-implications] and
Lemma [lemma-stability]. Since $C_{\mathfrak m}$ is strictly
henselian, Olivier's theorem identifies it with $D_{\mathfrak n}$.
Every prime of $D$ is contained in a maximal ideal, so further
localization identifies the local rings at every prime. The
ind-Zariski criterion for w-local rings now applies: a map which
identifies local rings and sends closed points to closed points on
spectra is ind-Zariski. Its proof uses the description of w-local
spectra by their components in [proposition-w-local-components],
realizes the pullback along $\pi_0(\operatorname{Spec}(D))\to
\pi_0(\operatorname{Spec}(C))$ by an ind-Zariski $C$-algebra,
and identifies this algebra with $D$ using the local rings and
connected components. Thus $C\to D$ is ind-Zariski.
It follows that both $R\to C\to D$ and $B\to D'\to D$ are
ind-étale.

It remains to prove faithful flatness over $B$. The closed points
$V(J)$ of $\operatorname{Spec}(C)$ map onto
$\operatorname{Spec}(R)$: the w-localization supplies a closed point
over each prime of $R$, which lifts through the faithfully flat
ind-étale contraction and the final w-localization. Base change
therefore makes

$$
\operatorname{Spec}\bigl(B\otimes_R(C/J)\bigr)
\longrightarrow\operatorname{Spec}(B)
$$

surjective. Each resulting prime of $D'$ containing $K$ lifts to
$D$, because w-localization along $K$ induces a bijection on the
corresponding zero loci. Hence $\operatorname{Spec}(D)\to
\operatorname{Spec}(B)$ is surjective. Together with flatness of the
ind-étale map $B\to D$, this proves faithful flatness.
