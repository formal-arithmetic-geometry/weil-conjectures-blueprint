+++
kind = "proof"
of = "det-brown-hypotheses-ambient"
+++
*Locally small.* $\Mod(X_{\mathrm{proét}},\Lambda)$ is a Grothendieck abelian category, so its unbounded derived
category $\D(X_{\mathrm{proét}},\Lambda)$ exists with small Hom sets (Hom sets are computed via K-injective
resolutions, which exist in a Grothendieck category). A full subcategory has the same Hom sets.

*Triangulated with sums.* $\Loc(\Dctf(X,\Lambda))$ is by definition ([sk-def-localizing-closure]) a full
triangulated subcategory closed under the direct sums of $\D(X_{\mathrm{proét}},\Lambda)$, which exist (termwise
sums of complexes); so it has arbitrary direct sums, computed in the ambient category.

*Idempotents.* A triangulated category with countable direct sums is idempotent complete ([Stacks, Tag 05QW](https://stacks.math.columbia.edu/tag/05QW)): for $e\colon K\to K$ idempotent, the homotopy colimit of $K\xrightarrow{e}K\xrightarrow{e}\cdots$, the cone
of $1-\mathrm{shift}$ on $\bigoplus_{\mathbf N}K$, is an image of $e$. This homotopy colimit is built from sums
and a cone, hence lies in $\Loc(\Dctf(X,\Lambda))$.
