+++
kind  = "proof"
of    = "sk-prop-av-fixed-base-change"
+++
Choose a $k$-basis and write $F(e_j)=\sum_ia_{ij}e_i$ with
$a_{ij}\in k$. The fixed points are the solutions in $(k')^n$ of the
system $x_i=\sum_ja_{ij}x_j^p$, whose coefficients lie in $k$. By the
block decomposition used in [sk-prop-av-lang-steinberg], the equations
express $x_i=\sum_{k\le i}a_k^{p^{\,i-k}}x_m^{p^{\,i-k+1}}$ as
polynomials in $x_m$ with coefficients in $k$, and the remaining
equation is $\varphi(x_m)=0$ for a nonzero polynomial $\varphi\in k[X]$; all its roots lie in the algebraically closed field $k$. The
two solution sets therefore agree blockwise, and the map is injective,
so it is an isomorphism.
