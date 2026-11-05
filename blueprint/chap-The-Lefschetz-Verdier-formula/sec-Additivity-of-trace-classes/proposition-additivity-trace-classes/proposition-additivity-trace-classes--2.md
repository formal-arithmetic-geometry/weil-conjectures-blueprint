+++
id = "proposition-additivity-trace-classes--2"
kind = "proposition"
title = "Additivity at a fixed rational point"
name_showing = false
order = 942003
aliases = ["bp-r287-2"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_ofGraph_eq_add"]
uses = ["definition-correspondence", "definition-trace-class-local-terms", "definition-pushforward-correspondence"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime,
and let $X$ be a separated $k$-scheme of finite type. Let $h:X\to X$
be a $k$-endomorphism, $x:\Spec k\to X$ a rational point with
$h\circ x=x$, and $j:U=X\setminus\{x\}\to X$ its open complement.
For $K\in\Dctf(X,\Qbarl)$ and a morphism $v:h^*K\to K$, put

$$
c=(\id_X,h):X\longrightarrow X\times X,
\qquad K_U=j_!j^*K,\qquad K_Z=Rx_*x^*K.
$$

Let $v_x:x^*K\simeq x^*h^*K\to x^*K$ be the stalk map induced by
$v$, and let $u_Z:h^*K_Z\to\id_X^!K_Z$ be its proper pushforward
along $(x,x)$ as in Definition [definition-pushforward-correspondence].
Put $V=h^{-1}(U)$, with inclusions $j_V:V\to X$ and $\iota:V\to U$
and restriction $h_V:V\to U$. The map $u_U:h^*K_U\to\id_X^!K_U$
is the composite

$$
h^*j_!j^*K\simeq j_{V!}h_V^*j^*K
\simeq j_!\iota_!h_V^*j^*K
\longrightarrow j_!j^*K\simeq\id_X^!K_U,
$$

where the middle arrow is induced by the $\iota_!\dashv\iota^*$
adjoint of $h_V^*j^*K\simeq j_V^*h^*K\to j_V^*K\simeq\iota^*j^*K$.
Then, viewing $v$ as a coefficient map through $K\simeq\id_X^!K$,

$$
\operatorname{Tr}_c(v)=\operatorname{Tr}_c(u_Z)+\operatorname{Tr}_c(u_U)
\quad\text{in }H^0(\Fix(c),\omega_{\Fix(c)}).
$$

No invertibility of $v$ or properness of $h$ is assumed.
