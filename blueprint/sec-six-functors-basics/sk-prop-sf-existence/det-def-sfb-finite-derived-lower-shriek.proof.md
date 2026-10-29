+++
kind  = "proof"
of    = "det-def-sfb-finite-derived-lower-shriek"
+++
The functors are [def-sfb-finite-derived-lower-shriek-compactification],
[def-sfb-finite-derived-lower-shriek] and [def-sfb-finite-derived-lower-shriek-plus]. The
compatibility with the inclusions is [def-sfb-finite-derived-lower-shriek-plus-compat], and
$R\Gamma$ and $R\Gamma_c$ are [def-sfb-finite-derived-global-sections] and
[def-sfb-finite-compactly-supported].

$R(g_*\circ i_!)$ would be computed by applying $g_*i_!$ to a K-injective resolution
$K\to I$. The extension by zero $i_!$ does not send injective sheaves to $g_*$-acyclic
ones, so $g_*i_!I$ need not compute $Rg_*(i_!K)$, and the two functors differ in
general. The composite $Rg_*\circ D(i_!)$ is the one built from the two adjunctions
$D(i_!)\dashv D(i^*)$ and $Rg_*\dashv Rg^!$, which is what gives $Rf_!$ a right adjoint.
In degree $0$ they agree: for a sheaf
$F$, $H^0(Rg_*(i_!F))=g_*(i_!F)=f_!F$ since $g_*$ is left exact.
