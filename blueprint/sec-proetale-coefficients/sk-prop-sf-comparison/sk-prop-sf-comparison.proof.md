+++
kind = "proof"
of = "sk-prop-sf-comparison"
uses = ["sk-lem-pe-injective-acyclicity", "sk-thm-pe-classical-sheaves"]
+++
Choose a bounded-below injective resolution $I^\bullet$ of $K$. By
[sk-lem-pe-injective-acyclicity], $\nu_X^*I^\bullet$ is a resolution by
$\nu_{X,*}$-acyclic sheaves, so applying $\nu_{X,*}$ termwise computes
$R\nu_{X,*}\nu_X^*K$. By [sk-thm-pe-classical-sheaves] the underived unit is an
isomorphism on every term, so
this complex is $I^\bullet$, which proves that the derived unit
$K\to R\nu_{X,*}\nu_X^*K$ is an isomorphism (Stacks, Tag 099V). Full
faithfulness follows by adjunction. Composing derived right adjoints,
$R\Gamma(X_{\mathrm{proét}},-)=R\Gamma(X_{\mathrm{ét}},-)\circ R\nu_{X,*}$, gives
the statement on global sections (Stacks, Tag 099W).

For the affine formula, apply the global sections statement to $U$ and then
continuity of étale cohomology under affine limits (Stacks, Tag 03Q6). This
gives the formula in each degree for a sheaf. For a bounded-below complex
only finitely many terms of the hypercohomology spectral sequence contribute
to each total degree, and filtered colimits are exact.
