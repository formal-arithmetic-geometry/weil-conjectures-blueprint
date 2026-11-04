+++
kind = "proof"
of = "lemma-hypotheses-brown-representability"
order = 519
uses = ["theorem-compactness-rational-coefficients", "proposition-compactness-finite-coefficients", "proposition-compactness-proper-direct-image"]
+++
The set-theoretic conditions are general facts about derived categories
of Grothendieck abelian categories. Compactness was proved separately
for each kind of coefficients. Generation follows from the
definition of the localizing category.

As the derived category of a Grothendieck abelian category of module
sheaves, the ambient category is locally small, and so is its
full subcategory $\Loc(D^b_{\mathrm{ctf}}(-,\Lambda))$. The latter has direct sums by
definition, so its idempotents split [Stacks, [05QW](https://stacks.math.columbia.edu/tag/05QW)]. The subcategory
$D^b_{\mathrm{ctf}}(X,\Lambda)$ is thick, since constructibility and finite Tor
amplitude are preserved by shifts, cones and direct summands.

To see that $D^b_{\mathrm{ctf}}(X,\Lambda)$ is essentially small, note first that the
constructible sheaves in the heart have a set of representatives for each
admissible $\Lambda$. A bounded complex with such cohomology is built from its
cohomology sheaves by finitely many extensions, formed with truncations
in the ambient category. Each extension step is classified by an
element of a Hom set of the ambient category, and these Hom sets are
sets because the ambient category is locally small. Hence these
complexes form an essentially small category, of which
$D^b_{\mathrm{ctf}}(X,\Lambda)$ is a full subcategory.

Compactness for finite $A$ is Proposition [proposition-compactness-finite-coefficients].
For $E$ and $\overline{\mathbf Q}_\ell$ it is
Theorem [theorem-compactness-rational-coefficients], and for $\mathcal O_E$
it is Proposition [proposition-compactness-proper-direct-image]; in the integral and rational cases,
$D^b_{\mathrm{ctf}}=\Dbc$.

For generation, suppose that $K\in\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ receives no
nonzero maps from shifts of objects of a small skeleton. The objects
$M$ with $\Hom(M[n],K)=0$ for all $n$ form a localizing subcategory
containing $D^b_{\mathrm{ctf}}$. Hence this subcategory contains $K$. Then $\mathrm{id}_K=0$, and so $K=0$.
