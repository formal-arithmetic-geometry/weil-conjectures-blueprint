+++
kind = "proof"
of = "sk-prop-proper-image-localizing"
uses = ["sk-lem-proper-unbounded-window", "sk-thm-sfb-proper-base-change", "sk-prop-ctf-finite-proper", "sk-prop-int-compactness", "sk-lem-int-tensor"]
+++
For $E$ and $\overline{\mathbf Q}_\ell$, Lemma [sk-lem-proper-unbounded-window](3)
shows that $Rp_*$ preserves direct sums on
$\Dic(X,\Lambda)\supset\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$, and
Proposition [sk-thm-sfb-proper-base-change] shows that $Rp_*$ preserves
$D^b_{\mathrm{ctf}}=\Dbc$. For finite $A$, the corresponding two facts are
Proposition [sk-prop-ctf-finite-proper], and for $\mathcal O_E$, they are
Proposition [sk-prop-int-compactness] and Proposition [sk-thm-sfb-proper-base-change]. In each case, the
objects
$K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ with
$Rp_*K\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ form a triangulated subcategory closed
under direct sums and containing $D^b_{\mathrm{ctf}}(X,\Lambda)$, and hence they form all of
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$.

Extension by zero is exact and left adjoint to $j^*$, and hence it preserves
direct sums. To see that it preserves constructibility, add the closed
complement as a stratum on which the sheaf is zero. For finite $A$, it also
preserves finite Tor amplitude, as one checks on stalks. For
$\mathcal O_E$, $E$ and $\overline{\mathbf Q}_\ell$ we have $D^b_{\mathrm{ctf}}=\Dbc$, so constructibility
suffices (for $\mathcal O_E$ this is Lemma [sk-lem-int-tensor]). Therefore the same argument
with localizing subcategories shows that $j_!$ restricts as stated.
