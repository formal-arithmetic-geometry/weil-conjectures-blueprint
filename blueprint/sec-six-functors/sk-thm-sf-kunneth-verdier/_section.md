+++
id = "sk-thm-sf-kunneth-verdier"
kind = "lemma"
title = "External duality and the trace morphism"
order = 3516
uses = ["sk-def-ops", "sk-lem-sf-kunneth-star", "sk-thm-pd-verdier-duality", "sk-thm-sf-ctf-stability", "sk-def-sf-kv-maps", "sk-prop-sf-open-closed-triangle", "sk-lem-sf-flat-model", "sk-lem-sf-mate", "sk-prop-sf-closed-unit", "sk-prop-sf-dualizable-biduality", "sk-prop-sf-localization", "sk-thm-regular", "sk-thm-sf-tensor-hom", "sk-thm-smooth-purity", "sk-prop-integral-criterion", "sk-prop-sf-comp-coherence", "sk-thm-sbc-coefficients"]
lean = ["AlgebraicGeometry.Etale.hasKunnethComparisons"]
tags = ["sketch"]
+++
Here $k=\overline{\mathbf F}_q$, $A$ is a finite commutative $\ell$-primary ring with
$\ell\ne\operatorname{char}k$, $X$ is a separated $k$-scheme of finite type, and
$\omega_X$ and $\mathbb D_X$ are the dualizing complex and the Verdier dual of
Definition [sk-def-ops] with coefficients $A$. A *correspondence* on $X$ is a morphism
of $k$-schemes $c=(c_1,c_2):C\to X\times X$; its *fixed locus* is the closed subscheme
$F_c=C\times_{X\times X,\Delta_X}X$, with projections $i_c:F_c\to C$, a closed
immersion, and $d_c:F_c\to X$.

Let $K\in\Dctf(X,A)$, let $p_1,p_2:X\times X\to X$ be the projections, and put
$P_X=K\boxtimes\mathbb D_XK\in\Dctf(X\times X,A)$. For a correspondence
$c:C\to X\times X$ there are canonical isomorphisms, in $\Dctf(X\times X,A)$ and in
$\Dctf(C,A)$,

$$
P_X\xrightarrow{\sim}\cHom_A(p_2^*K,p_1^!K),
\qquad
\mathcal H_c(K):=\cHom_A(c_2^*K,c_1^!K)
\xrightarrow{\sim}c^!P_X.
$$

Diagonal evaluation therefore gives a morphism in
$D(C_{\mathrm{pro\acute et}},A)$, the *trace morphism*,

$$
\mathcal H_c(K)\longrightarrow Ri_{c*}\omega_{F_c}.
$$

*General form.* The three maps of [sk-def-sf-kv-maps] are isomorphisms, natural in their
variables, under the hypotheses of that definition (the $Rf_i^!$ are the
constructible exceptional adjoints of [det-def-sf-operations] (vi); no
admissibility datum of [det-def-sf-admissible] is assumed): the
exceptional Künneth map $\alpha$, the external Hom map $\beta$, and the
Künneth–Verdier map $\kappa$. In particular, for $X,Y$ separated of finite
type over $k$, with the structure
morphism $a_Y$ and the product projection $p_X=\operatorname{id}_X\times a_Y$
as in [sk-def-sf-kv-maps] (iv), and
$M\in\Dctf(X,\Lambda)$, $N\in\Dctf(Y,\Lambda)$,

$$
\kappa_{M,N}:M\boxtimes\mathbb D_YN\ \xrightarrow{\ \sim\ }\
\RHom\bigl(p_Y^*N,Rp_X^!M\bigr).
$$
