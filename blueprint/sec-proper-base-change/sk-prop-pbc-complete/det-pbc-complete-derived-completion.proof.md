+++
kind = "proof"
of = "det-pbc-complete-derived-completion"
uses = ["def-weil-derived-limit"]
+++
For every $M$ the canonical map $M\to R\varprojlim_nM_n$ to a homotopy limit of
the tower of reductions has a cone $Z$ on which $\varpi$ acts invertibly, and
$R\varprojlim_nM_n$ is derived complete. Derived complete objects are right
orthogonal to the objects on which $\varpi$ acts invertibly, so for every derived
complete $N$, composition with $M\to R\varprojlim_nM_n$ is a bijection
$\operatorname{Hom}(R\varprojlim_nM_n,N)\cong\operatorname{Hom}(M,N)$ (long exact
$\operatorname{Hom}$ sequence of the triangle). Hence
$M\mapsto R\varprojlim_nM_n$ is a reflection into the derived complete objects,
which defines the left adjoint $\widehat{(-)}$ with unit $\kappa$ (homotopy limits
are not functorial, but the reflection is, by its universal property). Since
$\varpi$ is a nonzerodivisor, $R/I^n$ has the two-term free resolution
$[R\xrightarrow{\varpi^n}R]$, so $Z\otimes^{\mathbf L}R/I^n$ is the cone of
$\varpi^n$ on $Z$, which is zero; thus $\kappa_M\otimes^{\mathbf L}R/I^n$ is an
isomorphism. If $M$ is derived complete, $\kappa_M$ is an isomorphism because it is
the unit of a reflection at an object of the subcategory; conversely $\widehat M$ is
derived complete.
