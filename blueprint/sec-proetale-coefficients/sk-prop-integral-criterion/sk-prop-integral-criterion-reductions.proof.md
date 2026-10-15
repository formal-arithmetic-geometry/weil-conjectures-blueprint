+++
kind  = "proof"
of    = "det-prop-integral-criterion-reductions"
+++
$(2)\Rightarrow(1)$ is the case $n=1$.

$(1)\Rightarrow(2)$. Suppose $K_1$ has cohomology in $[r,s]$, with constructible cohomology
sheaves. The exact sequences $0\to\cO_E/\pi_E^{n-1}\xrightarrow{\pi_E}\cO_E/\pi_E^n\to\cO_E/\pi_E\to0$
give, after $K\otimes^{\mathbf L}-$, distinguished triangles
$K_{n-1}\to K_n\to K_1\to K_{n-1}[1]$. By induction on $n$ and the long exact cohomology
sequence, $K_n$ has cohomology in $[r,s]$, and each $H^q(K_n)$ is an extension of a
subsheaf of $H^q(K_1)$ by a quotient of $H^q(K_{n-1})$: precisely, of
$\ker(H^q(K_1)\to H^{q+1}(K_{n-1}))$ by $\coker(H^{q-1}(K_1)\to H^q(K_{n-1}))$. With torsion
coefficients on a Noetherian scheme constructible sheaves are closed under kernels,
cokernels and extensions (the classical finite-stalk theory), regarding
$\cO_E/\pi_E$-modules as $\cO_E/\pi_E^n$-modules by restriction of scalars, which preserves
constructibility. Hence $H^q(K_n)$ is constructible and $K_n\in\Dbc(X,\cO_E/\pi_E^n)$, with
the uniform interval $[r,s]$.
