+++
kind = "proof"
of = "lemma-extension-across-finite-subset--1"
order = 576002
uses = ["lemma-detection-proper-direct-image", "theorem-proper-base-change-classical-pro", "lemma-identity-pasting"]
+++
The scheme $S$ is noetherian, and so is $U$. For every $T\to S$ with
image in $U$, the map $Z_T\to T$ is finite, since it is obtained by
base change from $Z\times_S U\to U$.

First take $T=U$. Base change along the open immersion $G\hookrightarrow Y$
identifies $(Rj_{U,*}K_U)|_{G_U}$ with $Rj_{G,U,*}K_{G,U}$, which is
bounded constructible by hypothesis. The composition isomorphism

$$
Rb_{U,*}Rj_{U,*}K_U\simeq Ra_{U,*}K_U
$$

identifies the direct image to $U$ with another bounded constructible
complex. The finite-ring form of part (1) of
[lemma-detection-proper-direct-image] gives
$Rj_{U,*}K_U\in\Dbc(Y_U,\Lambda)$.

Now let $T$ be any noetherian scheme with a map $t:T\to S$ whose image
is contained in $U$, and let
$\varphi:g_Y^*Rj_*K\to Rj_{T,*}K_T$ be the base change map.
Base change along open immersions and the pasting law
[lemma-identity-pasting] identify its restriction to $G_T$ with the
base change map for $j_G$, so this restriction is an isomorphism.
Proper base change for $b$, in the étale form of
[theorem-proper-base-change-classical-pro], applies because $\Lambda$
is finite. Together with vertical pasting [lemma-identity-pasting],
it identifies $Rb_{T,*}\varphi$, up to composition isomorphisms, with
the base change map for $a$. The latter is an isomorphism by hypothesis.
Part (2) of [lemma-detection-proper-direct-image], applied to $b_T$
and the finite boundary $Z_T$, now shows that $\varphi$ is an isomorphism.

Finally, $g_Y$ factors through $Y_U$. Pullback preserves bounded
constructibility. Pull back $Rj_{U,*}K_U$ along $Y_T\to Y_U$, and use
base change along $U\hookrightarrow S$ and the isomorphism $\varphi$
to identify the result with $Rj_{T,*}K_T$. This proves bounded
constructibility after every allowed base change.
