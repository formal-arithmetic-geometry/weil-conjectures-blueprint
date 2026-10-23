+++
kind  = "proof"
of    = "det-lem-picard-zero-dictionary"
uses = ["lem-sc-riemann-roch"]
+++
On a fibre $X_t$ the data
$Rf_{t,*}\cL_t\cong\cN_t[0]$ give $h^0(X_t,\cL_t)=1$ and
$h^q=0$ for $q>0$, so by [det-cor-picard-degree-g]:

$$
\deg(\cL_t)=\chi(\cL_t)-\chi(\cO_{X_t})=1-(1-g)=g .
$$

*(Two instances of [lem-sc-riemann-roch] (G) and the DVR argument.)*
$s_t\neq0$ (it is the identity of $\cN_t$), and over the fibre $X_t$,
which is integral because $X$ is geometrically integral over $k$, its
zero set is a finite effective Cartier divisor of degree
$\deg\cL_t=g$ (the local rings at its points are DVRs); the Cartier
criterion promotes this to the relative statement and gives that
$D\to T$ is finite locally free of degree $g$.
