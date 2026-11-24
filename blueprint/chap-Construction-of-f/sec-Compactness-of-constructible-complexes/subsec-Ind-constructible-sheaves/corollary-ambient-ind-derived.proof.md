+++
kind = "proof"
of = "corollary-ambient-ind-derived"
order = 460
+++
In the long exact cohomology sequence of a triangle, each cohomology
sheaf of the third term is an extension of a kernel by a cokernel of maps
between cohomology sheaves of the other two. Since [$\IndCons(X,\Lambda)$](@definition-ind-constructible-sheaves)
is closed under kernels, cokernels and extensions
(Proposition [proposition-ind-constructible-sheaves]), the third term lies in
$\Dic(X,\Lambda)$ whenever the other two do. Closure under shifts is
clear. As direct sums of sheaves are exact, $H^n$ commutes with direct
sums. Since [$\IndCons(X,\Lambda)$](@definition-ind-constructible-sheaves) is closed under direct sums, it follows that
$\Dic(X,\Lambda)$ is closed under direct sums. Truncation only
removes cohomology sheaves and keeps the others. Hence $\Dic(X,\Lambda)$ is a localizing
subcategory of $D(\href{@definition-small-pro-etale-site}{X_{\mathrm{pro}\acute{e}t}},\Lambda)$ containing [$\Dbc(X,\Lambda)$](@definition-constructible-sheaves). It
therefore contains the smallest one, [$\Loc(\Dbc(X,\Lambda))$](@definition-localizing-subcategory).
