+++
kind = "proof"
of = "det-sp-reduction-direct-image"
+++
*Step 1: the natural map.* For any $N\in D(\bar X_{\mathrm{proét}},A)$ there is
a natural projection map
$R\bar f_*N\otimes^{\mathbf L}_{A_Y}B_Y\to R\bar f_*(N\otimes^{\mathbf L}_{A_{\bar X}}B_{\bar X})$,
the transpose under $\bar f^*\dashv R\bar f_*$ of
$\bar f^*R\bar f_*N\otimes^{\mathbf L}B_{\bar X}\to N\otimes^{\mathbf L}B_{\bar X}$
(counit tensored with the identity, using $\bar f^*B_Y=B_{\bar X}$). Extension
by zero is exact and commutes with tensoring with the constant sheaf $B$:
$j_!(M)\otimes^{\mathbf L}B_{\bar X}\simeq j_!(M\otimes^{\mathbf L}B_X)$.
Define $b(M)$ as the composite with $N=j_!M$.

*Step 2: free terms.* Choose a resolution $F_\bullet\to B$ by finite free
$A$-modules, bounded above but possibly infinite to the left. Represent $M$ by
a bounded complex $P$ of flat constructible $A_X$-modules in degrees $[a,b]$
([lem-sf-flat-model]). Then $M_B$ is the total complex of
$j_!P\otimes_{A}F_\bullet$, and similarly on $Y$. For a free term
$F_{-i}=A^{r_i}$ the comparison map is the identity of
$(R\bar f_*j_!P)^{\oplus r_i}$, an isomorphism.

*Step 3: finite windows.* $R\bar f_*$ has cohomological dimension at most
$c=\operatorname{cd}_\ell(\bar f)<\infty$ on $\ell$-power torsion sheaves.
Hence in a fixed total degree $q$, only the terms $F_{-i}$ with
$a-i\leq q\leq b-i+c$, i.e. finitely many $i$, contribute to $H^q$ of either
side (truncate the resolution, the stupid truncation changing the totalization
only in degrees below $q$). On this finite window the comparison is a finite
extension of isomorphisms of Step 2, hence an isomorphism on $H^q$. As $q$ is
arbitrary, $b(M)$ is an isomorphism, regardless of the projective dimension of
$B$ over $A$; this is the scalar projection argument used for the
coefficient comparisons of the six operations.

*Step 4: naturality and composition.* Naturality in $M$ holds since every map
used is natural. For $A\to B\to C$, the projection maps of Step 1 compose under
the associativity isomorphism $(N_B)_C\simeq N_C$, because the counit
transposes compose; hence the stated cocycle identity holds.
