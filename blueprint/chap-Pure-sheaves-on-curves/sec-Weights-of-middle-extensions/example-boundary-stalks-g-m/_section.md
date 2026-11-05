+++
id = "example-boundary-stalks-g-m"
kind = "example"
title = "Boundary stalks on $\\mathbf G_m\\subset\\mathbf A^1$"
order = 1175
uses = ["example-kummer-extension"]
+++
Let $j:\mathbf G_{m,k_0}\hookrightarrow\mathbf A^1_{k_0}$ and $z=0$. The
covers $u^n=t$ are totally ramified at $0$, so the inertia $I_0$ maps onto
the monodromy of a Kummer sheaf. For the Kummer sheaf of a nontrivial
character, $I_0$ acts on the line $V$ through that character. Hence
$V^{I_0}=0$, and the stalk of $j_*$ of this sheaf at $\bar0$ is zero, so here
$j_*$ and $j_!$ agree.
For the Kummer extension $\mathcal E$ of
Example [example-kummer-extension], on the other hand, $I_0$ acts by the matrices
$\bigl(\begin{smallmatrix}1&\kappa\\0&1\end{smallmatrix}\bigr)$ with
$\kappa$ running over $\mathbf Z_\ell(1)$, whose common fixed vectors form the line
$\overline{\mathbf Q}_\ell(1)$. So the stalk of $j_*\mathcal E$ at $0$ is $\overline{\mathbf Q}_\ell(1)$, of weight
$-2$, while $\mathcal E$ has weights $-2$ and $0$; the stalk at the
boundary keeps only part of the weights.
