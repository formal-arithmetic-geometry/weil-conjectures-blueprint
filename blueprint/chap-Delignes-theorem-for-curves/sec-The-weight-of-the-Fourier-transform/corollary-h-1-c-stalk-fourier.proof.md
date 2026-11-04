+++
kind = "proof"
of = "corollary-h-1-c-stalk-fourier"
order = 1282
uses = ["lemma-boundary-stalk", "proposition-weights-j-boundary-points", "proposition-base-change-fourier-inversion", "theorem-weight-fourier-transform"]
+++
We compute the stalk at $0'$ of $\operatorname{FT}_\psi((j_*M)[1])$ in
two ways: by the stalk formula, which gives the cohomology of $j_*M$,
and through the isomorphism with $(j'_*M')[1]$, which gives a stalk of
a middle extension.

At the rational origin $0'$ of the dual line, the kernel
$\mathcal K_\psi$ restricts to the pullback of $\mathcal L_\psi$ along
the constant map to $0$, which is canonically trivial (on traces this
is $\psi(0)=1$). The stalk formula of
Proposition [proposition-base-change-fourier-inversion], which is
compatible with Frobenius, therefore gives

$$
\bigl(\operatorname{FT}_\psi((j_*M)[1])\bigr)_{0'}
=R\Gamma_c(\mathbf A^1,j_*M)[2].
$$

We compare this with the stalk of $(j'_*M')[1]$, which is concentrated
in degree $-1$. In degree $0$ we see that
$H_c^2(\mathbf A^1,j_*M)=0$. In degree $-1$ we obtain

$$
H_c^1(\mathbf A^1,j_*M)
\simeq(j'_*M')_{0'}
=(M'_{\bar\eta})^{I_{0'}},
$$

where $I_{0'}$ is the inertia group at the origin $0'$ of the dual line
acting on the generic fibre of $M'$, and the last equality is the formula
of Lemma [lemma-boundary-stalk] for the stalk of a middle extension.
By Proposition [proposition-weights-j-boundary-points]
the weights of this stalk are at most the weight of $M'$, which is
$w+1$ by Theorem [theorem-weight-fourier-transform].
