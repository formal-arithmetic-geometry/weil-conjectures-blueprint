+++
kind = "proof"
of = "det-sp-tower-bound-uniform"
+++
Tor amplitude of an object of $\Dctf(Y_{\mathrm{proét}},A)$ can be checked on
geometric stalks: $Rf_!M$ has Tor amplitude in $[a,b+2d]$ iff for every
geometric point $\bar y$ and every $A$-module $N$,
$(Rf_!M)_{\bar y}\otimes^{\mathbf L}_AN$ has cohomology in $[a,b+2d]$.
By compactly supported (proper) base change to $\bar y$ and the projection
formula,

$$
(Rf_!M)_{\bar y}\otimes^{\mathbf L}_AN\simeq
R\Gamma_c\bigl(X_{\bar y},M|_{X_{\bar y}}\otimes^{\mathbf L}_AN\bigr).
$$

The complex $M|_{X_{\bar y}}\otimes^{\mathbf L}_AN$ has cohomology sheaves in
degrees $[a,b]$, by the Tor amplitude of $M$. The functor $R\Gamma_c$ on a
separated finite type scheme of dimension $\leq d$ over a separably closed
field has cohomological amplitude $[0,2d]$ on torsion sheaves ([Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10)). By the hypercohomology spectral sequence the right-hand side has
cohomology in $[a,b+2d]$. The interval does not depend on $n$ when applied to
the levels $C_n$ (with $A=\mathcal O_E/\ell^n$), and by
[det-sp-tower-shriek-levels] these levels compute $Rf_{!,\bullet}C_\bullet$; the
cohomological bounds follow likewise (take $N=A$).
