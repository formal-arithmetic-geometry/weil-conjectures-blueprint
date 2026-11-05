+++
id = "proposition-additivity-trace-classes--1"
kind = "proposition"
title = "Additivity along a distinguished triangle"
name_showing = false
order = 942002
aliases = ["bp-r287-1"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.Correspondence.traceClass_eq_add_of_distTriang"]
uses = ["definition-correspondence", "definition-trace-class-local-terms", "definition-verdier-dual-evaluation"]
+++
The general finite filtered statement is bypassed by Lean, which uses the
following additivity statement for a distinguished triangle.

Let $k$ be a field of characteristic $p>0$, let $\ell\ne p$ be prime, and
let $X$ and $C$ be separated $k$-schemes of finite type. Let
$c=(c_1,c_2):C\to X\times X$ be a correspondence, and let

$$
K'\xrightarrow{\epsilon}K\xrightarrow{\eta}K''\longrightarrow K'[1]
$$

be a distinguished triangle in $\Dctf(X,\Qbarl)$. Suppose that
$u:c_2^*K\to c_1^!K$, $u':c_2^*K'\to c_1^!K'$ and
$u'':c_2^*K''\to c_1^!K''$ satisfy

$$
c_1^!(\epsilon)\circ u'=u\circ c_2^*(\epsilon),
\qquad
c_1^!(\eta)\circ u=u''\circ c_2^*(\eta).
$$

Write $\mathbb D_X$ for Verdier duality and $\Delta_X:X\to X\times X$
for the diagonal. Assume that the following four morphism groups in
$\Dctf(X\times X,\Qbarl)$ vanish:

$$
\begin{aligned}
\Hom(Rc_!\Qbarl_C,(K''\boxtimes\mathbb D_XK')[-1])&=0,\\
\Hom(K'\boxtimes\mathbb D_XK,(K''\boxtimes\mathbb D_XK')[-1])&=0,\\
\Hom(K\boxtimes\mathbb D_XK'',(K''\boxtimes\mathbb D_XK')[-1])&=0,\\
\Hom((K'\boxtimes\mathbb D_XK'')[1],R\Delta_{X*}\omega_X)&=0.
\end{aligned}
$$

Then, for the same fixed locus of $c$ and all three coefficient objects,

$$
\operatorname{Tr}_c(u)=\operatorname{Tr}_c(u')+\operatorname{Tr}_c(u'')
\quad\text{in }H^0(\Fix(c),\omega_{\Fix(c)}).
$$
