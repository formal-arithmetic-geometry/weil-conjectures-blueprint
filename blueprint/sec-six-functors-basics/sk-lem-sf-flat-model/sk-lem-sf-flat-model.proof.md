+++
kind = "proof"
of = "sk-lem-sf-flat-model"
uses = ["sk-cor-pe-finite-tor-comparison"]
+++
By [sk-cor-pe-finite-tor-comparison], $C=\nu_X^*C_{\mathrm{ét}}$ with
$C_{\mathrm{ét}}\in\Dctf(X_{\mathrm{ét}},A)$, where
$\nu_X^*:D(X_{\mathrm{ét}},A)\to D(X_{\mathrm{proét}},A)$ is the comparison
inverse image. The complex $C_{\mathrm{ét}}$ has a bounded flat model by
[Stacks, Tag 0F4M](https://stacks.math.columbia.edu/tag/0F4M). Since $\nu_X^*$
is exact on sheaves, it pulls this model back to a bounded flat constructible
model on $X_{\mathrm{proét}}$. We choose a common stratification on which its
finitely many terms are locally constant. Recall that a finite flat module
over the Noetherian ring $A$ is finite projective. If $F$ is a flat
constructible sheaf, then the exact sequences for the successive open and
closed strata express $F$ as a finite extension of the sheaves $a_!L$ attached
to its strata. Similarly, the stupid filtration of the bounded flat complex
expresses $C$ as a finite extension of shifts of its *terms*. Both of these
operations preserve finite Tor amplitude. The same argument proves the
corresponding statement on $X_{\mathrm{ét}}$, which is used in the proof of
compactness before passing to the pro-étale site.

Flat models are needed because the cohomology sheaves of an object of $\Dctf$
can have infinite Tor amplitude. For example, the complex of constant sheaves
$[A\xrightarrow{\ell}A]$ with $A=\mathbf Z/\ell^2\mathbf Z$ is perfect, while
its nonzero cohomology sheaves are copies of $\mathbf F_\ell$, which have
infinite projective dimension over $A$. In other words, finite Tor amplitude
is a property of the complex, which can be read off from a flat model, and the
thick triangulated category $\Dctf$ is not the bounded derived category of an
abelian category of sheaves of finite Tor amplitude.
