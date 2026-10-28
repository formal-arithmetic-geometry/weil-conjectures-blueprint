+++
id = "prose-18-01"
kind = "hidden"
title = "Overview of the Fourier transform method"
order = 4140
+++
Let $M$ be a pure lisse sheaf on a dense open of the affine line, with
inclusion $j$. To bound the weights of $H^1_c(\mathbf A^1,j_*M)$, we
realize this group in the stalk at the origin of a complex on the dual
line, the Fourier transform of $j_*M$. The transform is the
sheaf-theoretic analogue of the discrete Fourier transform of
functions on $\mathbf F_q$,
$f\mapsto\bigl(y\mapsto\sum_xf(x)\psi(xy)\bigr)$: by the trace formula,
it transforms trace functions in this way, up to a sign
(see the formula in [sk-cor-plancherel]). For this to bound weights, the
transform must be, up to shift, the middle extension of a lisse sheaf
$M'$, so that it has a weight, and we must be able to compute that
weight from $M$. We meet the second requirement with the Plancherel
formula for squared trace sums, which detect the weight of a pure
sheaf. For the first, we prove in
Proposition [sk-p-dl-a1-middle] that if $M$ is irreducible and
no geometric constituent of $M$ is isomorphic to the pullback of the
additive character sheaf of the next subsection by a map
$x\mapsto ax$, then the transform of the middle extension $(j_*M)[1]$
is again a middle extension.

We use the six operations on the pro-étale site, first with
coefficients in a finite extension $E/\mathbf Q_\ell$ that contains
the $p$th roots of unity, $p$ being the characteristic of $k_0$, so
that it contains the values of the additive characters of $k_0$, and
then with coefficients in $\overline{\mathbf Q}_\ell$.

The kernel of the transform is a lisse sheaf whose trace function is
the additive character $\psi$, just as $\psi(xy)$ is the kernel of the
discrete transform. It is cut out of the Artin–Schreier cover of the
line as an eigenspace of the translations.
