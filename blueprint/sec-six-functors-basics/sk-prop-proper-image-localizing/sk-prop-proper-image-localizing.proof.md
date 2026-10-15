+++
kind = "proof"
of = "sk-prop-proper-image-localizing"
uses = ["sk-cor-ambient-ind-derived", "sk-def-sfb-dc-restricted-functors"]
+++
For $E$ and $\Qlb$, [sk-lem-proper-unbounded-window-ii] shows that $Rp_*$ preserves direct sums on
$\Dic(X,\Lambda)\supset\Loc(\Dctf(X,\Lambda))$ ([sk-cor-ambient-ind-derived]), and
[sk-thm-sfb-proper-base-change] gives preservation of $\Dctf=\Dbc$. For finite $A$, the corresponding two
facts are [sk-prop-ctf-finite-proper]; for $\mathcal O_E$, they are [sk-prop-int-compactness], using
$\Dctf=\Dbc$. In each case the objects $K\in\Loc(\Dctf(X,\Lambda))$ with $Rp_*K\in\Loc(\Dctf(Y,\Lambda))$
form a triangulated subcategory closed under direct sums and containing $\Dctf(X,\Lambda)$, hence all of
$\Loc(\Dctf(X,\Lambda))$ ([det-proper-image-localizing-principle], [det-proper-image-localizing-proper]).

Extension by zero is exact, is left adjoint to $j^*$ and preserves direct sums. It preserves
constructibility by adding the closed complement as a zero stratum. For finite $A$ it also preserves
finite Tor amplitude, as follows stalkwise from extension by zero ([lem-trf-open-ctf]); for $\mathcal O_E$, $E$
and $\Qlb$ this follows from the local models of constructible sheaves and [sk-def-sfb-dc-restricted-functors].
The same localizing argument therefore gives the stated restriction of $j_!$
([det-proper-image-localizing-open]).
