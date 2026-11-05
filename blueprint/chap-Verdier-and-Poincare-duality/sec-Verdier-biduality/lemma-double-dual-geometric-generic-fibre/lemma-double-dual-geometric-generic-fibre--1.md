+++
id = "lemma-double-dual-geometric-generic-fibre--1"
kind = "lemma"
title = "Generic pullback of dualizing complexes and biduality"
name_showing = false
order = 841001
aliases = ["bp-r252-1"]
lean = ["AlgebraicGeometry.Etale.exists_iso_leftDerivedUpperStar_dualizingComplex_of_generic", "AlgebraicGeometry.Etale.isIso_leftDerivedUpperStar_map_verdierDualDoubleDual_app_iff_of_generic"]
uses = ["definition-constructible-sheaves", "definition-relative-dualizing-complex", "definition-verdier-dual-evaluation", "definition-compactification-refinement"]
+++
Let $k$ be a field, let $B$ be an integral, quasi-separated scheme of finite
type over $k$ with structure morphism $a_B:B\to\operatorname{Spec}k$, and let
$A$ be a finite commutative ring whose exponent is invertible on $B$. Work on the small
étale sites. Assume that $\omega_B=a_B^!A$ is invertible for the derived
tensor product. Let $t:T\to B$ be a morphism from a noetherian scheme
such that every point of $T$ maps to the generic point of $B$.

Suppose that $f:X\to B$ factors as a closed immersion $i:X\hookrightarrow P$
followed by a smooth morphism $p:P\to B$ of pure relative dimension $r$.
Form the base changes $P'=P\times_B T$ and $X'=X\times_B T$, with maps
$g_P:P'\to P$, $p':P'\to T$, $g:X'\to X$ and $i':X'\hookrightarrow P'$.
Write $a_X=a_B\circ p\circ i$ and $f_T=p'\circ i'$.
Assume that $a_B,p,p',i,i',f,a_X,f_T$ admit compactifications and that
$a_B,p,f,a_X,f_T$ are quasi-compact. Set
$\omega_X=a_X^!A$ and $\omega_{X'/T}=f_T^!A$.

There is an invertible $L\in D(X'_{\acute{e}t},A)$ and an isomorphism

$$
g^*\omega_X\simeq\omega_{X'/T}\otimes_A^{\mathbf L}L.
$$

Suppose in addition that $k$ is perfect, that the exponent of $A$ is
invertible in $k$, and that $a_X$ is separated and of finite type. Let
$K\in D^b_{\mathrm{ctf}}(X,A)$, and assume that the monoidal structure on
$g^*$ respects the symmetry of the derived tensor product. Then

$$
g^*\delta_K\text{ is an isomorphism}
\quad\Longleftrightarrow\quad
\delta_{g^*K}\text{ is an isomorphism},
$$

where the two double-dual maps are formed using $\omega_X$ and
$\omega_{X'/T}$, respectively. The symmetry compatibility is supplied by
`AlgebraicGeometry.Etale.leftDerivedUpperStarBraided`.
