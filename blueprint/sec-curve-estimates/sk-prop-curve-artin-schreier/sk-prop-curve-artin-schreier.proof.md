+++
kind = "proof"
of = "sk-prop-curve-artin-schreier"
uses = ["sk-prop-av-fixed-points", "sk-prop-av-lang-steinberg", "sk-prop-av-fixed-base-change", "sk-prop-sf-comparison", "sk-thm-br", "sk-thm-curveestimate", "sk-prop-curve-affine-kummer"]
+++
On $C_{\mathrm{ét}}$ the Artin–Schreier sequence

$$
0\longrightarrow\mathbf F_p\longrightarrow\mathbf G_a
\xrightarrow{F-1}\mathbf G_a\longrightarrow0
$$

is exact; surjectivity is local because $T^p-T-a$ has derivative $-1$. The
étale cohomology of $\mathbf G_a$ is the coherent cohomology of $\cO_C$, by
faithfully flat descent on affine opens and the coherent Čech resolution.
Coherent cohomology vanishes above dimension one, and properness makes
$H^1(C,\cO_C)$ a finite-dimensional $k$-vector space.

The cohomology sequence is then controlled by a fact of linear algebra: if
$F$ is a Frobenius-linear endomorphism of a finite-dimensional $k$-vector
space $V$, then $F-1$ is surjective ([sk-prop-av-lang-steinberg]) and its
kernel is the set of $k$-points of a finite étale scheme of order $p^f$ with
$f\leq\dim_kV$ ([sk-prop-av-fixed-points]). To see this, reduce along a
finite filtration to the part where $F$ is nilpotent and the part where $F$
is bijective. On the nilpotent part $F-1$ is an additive polynomial
automorphism. On a bijective part of dimension $f$, choose a basis, invert
the matrix of $F$, and write the fibre equations as

$$
x_i^p-\sum_jb_{ij}x_j=c_i\qquad(1\leq i\leq f),
$$

where $(b_{ij})$ is invertible. The coordinate algebra is free of dimension
$p^f$, with basis the monomials having each exponent less than $p$. Its
Jacobian matrix is invertible, so it is finite étale and has $p^f$ points over
the algebraically closed field (Stacks, Tag 0A3L).

Apply this to $H^1(C,\cO_C)$ and to $H^0(C,\cO_C)=k$. The long exact
Artin–Schreier sequence gives the asserted formulas and vanishing. Under
$k'/k$, flat base change for coherent cohomology identifies the vector space
and its Frobenius-linear map with their scalar extensions. The kernel is a
finite étale scheme, whose $k$-points and $k'$-points agree, so the pullback
map itself is an isomorphism ([sk-prop-av-fixed-base-change]; Stacks, Tags
0HAN, 0A3P). [sk-prop-sf-comparison] returns the statement to
$C_{\mathrm{proét}}$.
