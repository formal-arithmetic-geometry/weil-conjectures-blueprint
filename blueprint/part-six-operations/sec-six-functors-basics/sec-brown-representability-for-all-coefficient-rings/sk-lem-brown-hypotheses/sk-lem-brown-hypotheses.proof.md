+++
kind = "proof"
of = "sk-lem-brown-hypotheses"
uses = ["sk-prop-ctf-finite-compact", "sk-thm-constructible-compactness", "sk-prop-int-compactness"]
+++
The ambient category is the derived category of a Grothendieck
abelian category of module sheaves. Hence it is locally small, and so is its
full subcategory $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$. The latter has direct sums by
definition, and therefore idempotents split [Stacks, Tag 05QW](https://stacks.math.columbia.edu/tag/05QW). The subcategory
$D^b_{\mathrm{ctf}}(X,\Lambda)$ is thick, since constructibility and finite Tor
amplitude are preserved by shifts, cones and direct summands. To see that $D^b_{\mathrm{ctf}}(X,\Lambda)$ is essentially small, note that the
constructible sheaves in the heart have a set of representatives for each
admissible $\Lambda$. A bounded complex with such cohomology is built from its
cohomology sheaves by finitely many extensions, formed with truncations
in the ambient category and classified by ambient Hom sets. These
complexes therefore form an essentially small category, and
$D^b_{\mathrm{ctf}}(X,\Lambda)$ is a full subcategory of it.

Compactness for finite $A$ is Proposition [sk-prop-ctf-finite-compact].
For $E$ and $\overline{\mathbf Q}_\ell$ it is
Theorem [sk-thm-constructible-compactness], and for $\mathcal O_E$
it is Proposition [sk-prop-int-compactness] (in the integral and rational cases,
$D^b_{\mathrm{ctf}}=\Dbc$). Finally, suppose that $K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ receives no
nonzero maps from shifts of objects of a small skeleton. The objects
$M$ with $\Hom(M[n],K)=0$ for all $n$ form a localizing subcategory
containing $D^b_{\mathrm{ctf}}$, hence containing $K$. Thus $\mathrm{id}_K=0$, and
we conclude that the skeleton generates.
