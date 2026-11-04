+++
kind = "proof"
of = "proposition-p-torsion-smooth-proper-curve"
order = 1579
uses = ["definition-ind-etale-pro-etale-weakly", "proposition-etale-implications", "lemma-stability", "definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map", "definition-derived-base-change-map", "lemma-identity-pasting", "lemma-acyclic-resolutions", "lemma-finite-morphisms", "theorem-smooth-base-change-classical-torsion", "definition-compactification-refinement", "theorem-nagata-s-compactification-theorem", "lemma-schematic-closure-uniqueness", "lemma-uniqueness-maps-dense-open", "theorem-chow-s-lemma-projective-form", "definition-abelian-variety", "lemma-abelian-variety-commutative", "lemma-symmetric-ample-sheaf", "proposition-pullback-multiplication-n", "proposition-multiplication-n", "definition-tate-module", "definition-relative-picard-functor", "theorem-riemann-roch-coherent-serre-duality", "corollary-serre-duality-field-extension", "theorem-picard-scheme-jacobian-over-separably", "corollary-degree-jacobian", "lemma-cohomology-multiplicative-group", "proposition-cohomology-smooth-affine-curve", "lemma-p-torsion-affine-curve-characteristic"]
+++
The Artin–Schreier sequence turns the question into one about
$\varphi-1$ on $H^0(C,\mathcal O_C)=k$ and on $H^1(C,\mathcal O_C)$. The
key fact is that on a finite-dimensional space over an algebraically
closed field, a Frobenius-linear map minus the identity is surjective
with finite kernel.

*Step 1: the Artin–Schreier sequence.* Write also $\varphi$ for the
endomorphism $a\mapsto a^p$ of the sheaf
$\mathbf G_a$ on $C_{\acute{e}t}$.  The Artin–Schreier sequence

$$
0\longrightarrow\mathbf F_p\longrightarrow\mathbf G_a
\xrightarrow{\varphi-1}\mathbf G_a\longrightarrow0
$$

is exact, because surjectivity is a local question and $T^p-T-a$ has
derivative $-1$. The étale cohomology of $\mathbf G_a$ is the
coherent cohomology of $\mathcal O_C$. Indeed, quasi-coherent sheaves have
the same cohomology on the étale and on the Zariski site, by faithfully
flat descent on affine opens and the Čech resolution. This coherent
cohomology vanishes in degrees above one, since $C$ is a curve. Since $C$
is proper, $H^1(C,\mathcal O_C)$ is a finite-dimensional $k$-vector space.

*Step 2: linear algebra.* Let $\varphi$ be a Frobenius-linear endomorphism of a
finite-dimensional $k$-vector space $V$; we show that $\varphi-1$ is surjective and that
its kernel is the set of $k$-points of a finite étale scheme of
order $p^f$ with $f\leq\dim_k V$.  We reduce along a finite
filtration to the part where $\varphi$ is nilpotent and the part where $\varphi$ is
bijective.  On the nilpotent part, $\varphi-1$ is an automorphism given by an
additive polynomial, with inverse $-(1+\varphi+\varphi^2+\cdots)$, a
finite sum; in particular its kernel there is zero.  On a bijective part of dimension $f$, we choose a
basis, invert the matrix of $\varphi$, and write the equations of the fibres as

$$
x_i^p-\sum_j b_{ij}x_j=c_i\qquad(1\leq i\leq f),
$$

where $(b_{ij})$ is invertible.  The coordinate algebra is free of
dimension $p^f$, with basis the monomials having each exponent less
than $p$.  The Jacobian matrix of these equations
is $-(b_{ij})$, because $p=0$ in $k$, and it is invertible; so each fibre is finite
étale of degree $p^f$ and has $p^f$ points over the algebraically
closed field $k$ [Stacks, [0A3L](https://stacks.math.columbia.edu/tag/0A3L)]. In particular every fibre is nonempty,
so $\varphi-1$ is surjective, and the kernel has $p^f$ elements.

*Step 3: conclusion.* We apply Step 2 to $H^0(C,\mathcal O_C)=k$ and to
$H^1(C,\mathcal O_C)$ in the long
exact sequence associated to the Artin–Schreier sequence. Surjectivity
of $\varphi-1$ on $H^0$ gives $H^1(C,\mathbf F_p)=\ker(\varphi-1)$ on
$H^1(C,\mathcal O_C)$, with the bound on its dimension, and surjectivity on
$H^1$ together with $H^2(C,\mathcal O_C)=0$ gives $H^q(C,\mathbf F_p)=0$ for
$q>1$. The pullback map under an extension $k'/k$ is an isomorphism
[Stacks, [0HAN](https://stacks.math.columbia.edu/tag/0HAN), [0A3P](https://stacks.math.columbia.edu/tag/0A3P)]: flat base change for coherent cohomology identifies the
vector space and its Frobenius-linear map with their scalar
extensions, and the kernel is a finite étale scheme, whose $k$-points
and $k'$-points agree. Finally,
Theorem [theorem-bounded-below-cohomology-comparison] carries the
statement over to $C_{\mathrm{pro}\acute{e}t}$.
