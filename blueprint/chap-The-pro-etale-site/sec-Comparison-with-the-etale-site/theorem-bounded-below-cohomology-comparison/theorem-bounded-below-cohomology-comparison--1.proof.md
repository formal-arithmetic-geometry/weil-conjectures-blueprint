+++
kind = "proof"
of = "theorem-bounded-below-cohomology-comparison--1"
order = 123004
uses = ["proposition-comparison-morphism-inverse-image", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "lemma-acyclic-resolutions"]
+++
Represent $K$ by a bounded below complex $I^\bullet$ of injective sheaves.
The comparison unit on sheaves is invertible by
[theorem-classical-sheaves-essential-image], so
$I^\bullet\to\nu_{X,*}\nu_X^*I^\bullet$ is an isomorphism termwise.
Exactness of $\nu_X^*$, from [proposition-comparison-morphism-inverse-image],
identifies $\nu_X^*I^\bullet$ with the derived inverse image of $K$.
Its terms are $\nu_{X,*}$-acyclic by
[lemma-acyclicity-pulled-back-injectives]. Thus [lemma-acyclic-resolutions]
makes the comparison
$\nu_{X,*}\nu_X^*I^\bullet\to R\nu_{X,*}\nu_X^*I^\bullet$ invertible.

The unit of the bounded below derived adjunction factors as these two maps.
Naturality transports its invertibility from $I^\bullet$ to $K$.
Finally, the inclusions of the bounded below derived categories into the
unbounded ones identify this unit with the unit of
$\nu_X^*\dashv R\nu_{X,*}$ at $K$, giving the stated isomorphism.
