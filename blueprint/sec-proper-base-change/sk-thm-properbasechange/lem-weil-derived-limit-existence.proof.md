+++
kind  = "proof"
of    = "lem-weil-derived-limit-existence"
+++
Assertion (1) is axiom TR1 applied to the defining triangle of
[def-weil-derived-limit], together with TR3 for the uniqueness of a cone;
this is Definition 13.34.1 of the Stacks Project, Tag
[08TC](https://stacks.math.columbia.edu/tag/08TC) and the remarks following
it, and it also explains why a derived limit is determined only up to a
non-unique isomorphism. Assertion (2) is Lemma 13.34.2 of the Stacks Project,
Tag [07KC](https://stacks.math.columbia.edu/tag/07KC): since countable
products are exact in $\mathcal A$, the termwise product of representatives
represents the product in $D(\mathcal A)$, and its cohomology is the product
of the cohomologies. Assertion (3) is the K-injective presentation of the
right derived functor of $\varprojlim$. The Stacks Project form of the model
statement is Lemma 13.34.6, Tag
[070M](https://stacks.math.columbia.edu/tag/070M), which treats the
truncation tower $I_n$ built from a single complex $K^\bullet$ by the
construction of Lemma 13.29.3 and concludes that $\varprojlim_nI_n$ exists,
is K-injective, and represents $R\varprojlim_n\tau_{\ge-n}K^\bullet$; the
general-tower form used here is the same argument applied to a K-injective
replacement of the given tower. Its inputs are that a product of K-injective
complexes is K-injective (Tag
[0BK6](https://stacks.math.columbia.edu/tag/0BK6), Lemma 13.31.5, stated
there without a bounded-below hypothesis, only that the termwise products
exist) and that every complex of the ambient category admits a K-injective
resolution: for a Grothendieck abelian category this is Tag
[079P](https://stacks.math.columbia.edu/tag/079P), Theorem 19.12.6, and the
ambient categories occurring in this blueprint are categories of sheaves of
modules, which are Grothendieck; the general form for an abelian category
with exact countable products and enough injectives is Spaltenstein's
theorem. The existence of the products used is Lemma 13.34.3, Tag
[0BK7](https://stacks.math.columbia.edu/tag/0BK7).
