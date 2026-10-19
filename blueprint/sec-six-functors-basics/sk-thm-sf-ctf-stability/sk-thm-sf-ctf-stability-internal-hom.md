+++
id = "det-thm-sf-ctf-stability-internal-hom"
kind = "lemma"
title = "Internal Hom on $\\Dctf$ for all admissible coefficient rings"
uses = ["det-thm-sf-ctf-stability-direct-images", "sk-lem-sf-flat-model", "sk-lem-int-tensor"]
+++
Let $\Lambda$ be admissible. For $K,L\in\Dctf(X,\Lambda)$,
$\cHom_\Lambda(K,L)\in\Dctf(X,\Lambda)$. More precisely, if
$a:S\hookrightarrow X$ is a locally closed immersion and $P$ a locally constant
perfect complex on $S$, then

$$
\cHom_X(a_!P,L)\simeq Ra_*\cHom_S(P,a^!L)\simeq Ra_*(P^\vee\otimes^{\mathbf L}a^!L),
\qquad P^\vee=\cHom_S(P,\Lambda_S),
$$

in $D(X_{\mathrm{proét}},\Lambda)$, and every $K\in\Dctf(X,\Lambda)$ is obtained
from finitely many objects $a_!P$ of this form by shifts and cones.
