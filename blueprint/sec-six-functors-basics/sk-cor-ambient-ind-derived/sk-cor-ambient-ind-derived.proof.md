+++
kind = "proof"
of = "sk-cor-ambient-ind-derived"
uses = ["sk-prop-ind-heart"]
+++
In the long exact cohomology sequence of a triangle, each cohomology sheaf of the third term is an
extension of a kernel by a cokernel of maps between cohomology sheaves of the other two, so
[sk-prop-ind-heart] implies closure under cones ([det-ambient-ind-derived-triangulated]). As direct sums
of sheaves are exact, $H^n$ commutes with direct sums, and truncation only removes cohomology sheaves.
Hence $\Dic(X,\Lambda)$ is a localizing subcategory of $\D(X_{\mathrm{proét}},\Lambda)$ containing
$\Dbc(X,\Lambda)$, and it therefore contains the smallest one, $\Loc(\Dbc(X,\Lambda))$
([det-ambient-ind-derived-sums]).
