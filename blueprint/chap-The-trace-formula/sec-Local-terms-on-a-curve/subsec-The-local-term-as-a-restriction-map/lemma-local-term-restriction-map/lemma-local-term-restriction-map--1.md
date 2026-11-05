+++
id = "lemma-local-term-restriction-map--1"
kind = "lemma"
title = "The local term as a restriction map (1)"
name_showing = false
order = 965001
aliases = ["bp-r294-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.supportedRestriction", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.FixedLocus.supportedEvaluation", "AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.localTerm_traceClass_eq_integral_supportedRestriction"]
uses = ["definition-constructible-sheaves", "definition-correspondence", "definition-verdier-dual-evaluation", "lemma-external-duality-trace-morphism", "definition-trace-class-local-terms", "proposition-six-operations-dctf", "proposition-composition-base-change-rf-shriek"]
+++
Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be a prime,
and put $\Lambda=\Qbarl$. Let $X$ and $C$ be separated schemes of finite
type over $k$, let $K\in D^b_c(X,\Lambda)$, and let
$c=(c_1,c_2):C\to X\times X$ be a correspondence with coefficient map
$u:c_2^*K\to c_1^!K$. Write $F=\Fix(c)$, with
$\iota:F\to C$ and $d:F\to X$, and let $\delta:X\to X\times X$ be
the diagonal. Thus the square $c\iota=\delta d$ is cartesian. Put
$P=K\boxtimes\mathbb D_XK$.

The tensor–Hom adjoint of $u$, followed by external duality
(Lemma [lemma-external-duality-trace-morphism]), gives the supported class

$$
[u]:\Lambda_C\longrightarrow
\cHom(c_2^*K,c_1^!K)\xrightarrow{\sim}c^!P.
$$

For any $P\in D^b_c(X\times X,\Lambda)$, the supported restriction
$\rho_P:\iota^*c^!P\to d^!\delta^*P$ is the
$\iota^*\dashv R\iota_*$ adjoint of

$$
c^!P\longrightarrow c^!R\delta_*\delta^*P
\xrightarrow{\sim}R\iota_*d^!\delta^*P,
$$

where the first map comes from the unit for $\delta^*\dashv R\delta_*$
and the second is base change in the fixed square. For
$P=K\boxtimes\mathbb D_XK$, define the supported evaluation by

$$
e_F:d^!\delta^*P\simeq d^!(K\otimes^{\mathbf L}\mathbb D_XK)
\xrightarrow{d^!\mathrm{ev}_K}d^!\omega_X\simeq\omega_F.
$$

Let $j:B\hookrightarrow F$ be open and closed, with $B$ proper over $k$.
Then the local term of Definition [definition-trace-class-local-terms]
is the integral over $B$ of the composite

$$
\Lambda_B\simeq j^*\iota^*\Lambda_C
\xrightarrow{j^*\iota^*[u]}j^*\iota^*c^!P
\xrightarrow{j^*\rho_P}j^*d^!\delta^*P
\xrightarrow{j^*e_F}j^*\omega_F
\simeq j^!\omega_F\simeq\omega_B.
$$

Here the identification $j^*\omega_F\simeq j^!\omega_F$ uses that $j$
is open. The formula applies to every such correspondence; it does not
require $X$ to be a curve or $c$ to be a Frobenius graph.
