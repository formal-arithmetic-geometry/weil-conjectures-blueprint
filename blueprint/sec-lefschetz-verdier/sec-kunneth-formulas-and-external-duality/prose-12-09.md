+++
id = "prose-12-09"
kind = "hidden"
title = "Künneth formulas and external duality"
order = 549
+++
A cohomological correspondence $u:c_2^*K\to c_1^!K$ is a morphism on
$C$. To obtain from it a class on the fixed locus, we must first view
it as a section of $c^!$ of a single complex on $X\times X$, which can
then be restricted to the diagonal. In linear algebra this is the
identification $\operatorname{Hom}(V,W)=W\otimes V^\vee$, under which
the trace becomes evaluation. Its sheaf version is the isomorphism
$\cHom(p_2^*K,p_1^!K)\simeq K\boxtimes\mathbb D_XK$ of
Lemma [sk-thm-sf-kunneth-verdier], and applying $c^!$ to it gives
$\cHom(c_2^*K,c_1^!K)$. On the point it is exactly
$\operatorname{Hom}(V,V)=V\otimes V^\vee$, and for $K=A_X$ with $X$
smooth of dimension $d$ both sides are $A(d)[2d]$.

This isomorphism combines Künneth formulas for $Rf_!$, $Rf_*$, $f^!$,
$\cHom$ and Verdier duals. The one for $Rf_!$ follows directly from
base change for compact supports and the projection formula. The one
for ordinary direct images is a base change statement for $Rf_*$, and
base change for $Rf_*$ fails in general: for
$j:\mathbf G_m\hookrightarrow\mathbf A^1$ the stalk of $Rj_*A$ at the
origin has cohomology $A$ in degree $0$ and $A(-1)$ in degree $1$,
while the fibre of $j$ over the origin is empty. Base change along a
product projection $Y\times T\to Y$ holds nevertheless
(Lemma [sk-lem-tf-independent-base-change]). After a compactification
only an open immersion remains, and for it the statement comes down to
base change along extensions of the ground field, a consequence of
smooth base change together with the Künneth formula with one proper
factor, which comes from proper base change. The formula for $f^!$
(Proposition [sk-prop-tf-exceptional-external-kunneth]) is proved by
dévissage on the coefficients, starting from constant coefficients,
where for smooth $f$ the functor $f^!$ is a twist and a shift.

The trace class is built from the external tensor product
$M\boxtimes N=p_1^*M\otimes^{\mathbf L} p_2^*N$ in $D((X\times X)_{\mathrm{pro}\acute{e}t},A)$, where
$p_1,p_2:X\times X\to X$ are the projections. Its construction
uses the Künneth formula for ordinary direct images
(Proposition [sk-lem-sf-kunneth-star]) and the corresponding
formula for Verdier duals (Lemma [sk-thm-sf-kunneth-verdier]). For an ordinary direct image along one
factor, the Künneth formula is a statement about base change
[tfbp-plus].
