+++
kind = "proof"
of = "sk-prop-proper-image-localizing"
uses = ["sk-lem-proper-unbounded-window", "sk-thm-sfb-proper-base-change", "sk-prop-ctf-finite-proper", "sk-prop-int-compactness", "sk-lem-int-tensor"]
+++
We use the definition of $\Loc(\Dctf(X,\Lambda))$ in the following form: if the objects of
$\Loc(\Dctf(X,\Lambda))$ with some property form a triangulated subcategory that is closed under direct
sums and contains $\Dctf(X,\Lambda)$, then every object of $\Loc(\Dctf(X,\Lambda))$ has the property
([det-proper-image-localizing-principle]).

For $E$ and $\Qlb$, part (3) of [sk-lem-proper-unbounded-window] shows that $Rp_*$ preserves direct sums
on $\Dic(X,\Lambda)\supset\Loc(\Dctf(X,\Lambda))$, and [sk-thm-sfb-proper-base-change] shows that $Rp_*$
preserves $\Dctf=\Dbc$. For finite $A$, the corresponding two facts are [sk-prop-ctf-finite-proper], and
for $\mathcal O_E$, they are [sk-prop-int-compactness] and [sk-thm-sfb-proper-base-change]. In each case,
the objects $K\in\Loc(\Dctf(X,\Lambda))$ with $Rp_*K\in\Loc(\Dctf(Y,\Lambda))$ form a triangulated
subcategory closed under direct sums and containing $\Dctf(X,\Lambda)$, and hence they form all of
$\Loc(\Dctf(X,\Lambda))$ ([det-proper-image-localizing-proper]).

Extension by zero is exact and left adjoint to $j^*$, and hence it preserves direct sums. To see that it
preserves constructibility, add the closed complement as a stratum on which the sheaf is zero. For finite
$A$, it also preserves finite Tor amplitude, as one checks on stalks. For $\mathcal O_E$, $E$ and $\Qlb$ we
have $\Dctf=\Dbc$, so constructibility suffices (for $\mathcal O_E$ this is [sk-lem-int-tensor]; see
[det-cor-int-compactness-ii]). Therefore the same argument with localizing subcategories shows that $j_!$
restricts as stated.
