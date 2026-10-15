+++
kind = "proof"
of = "sk-lem-sf-flat-model"
uses = ["sk-cor-pe-finite-tor-comparison"]
+++
By [sk-cor-pe-finite-tor-comparison], $C=\nu_X^*C_{\mathrm{ét}}$ with
$C_{\mathrm{ét}}\in\Dctf(X_{\mathrm{ét}},A)$, where
$\nu_X^*:D(X_{\mathrm{ét}},A)\to D(X_{\mathrm{proét}},A)$ is the comparison inverse
image. The complex $C_{\mathrm{ét}}$ has a bounded flat constructible model
(Stacks, Tag 0F4M, Lemma 59.77.3), and $\nu_X^*$, which is exact on sheaves,
pulls it back to a bounded flat constructible model on $X_{\mathrm{proét}}$.
Choose a common stratification on which its finitely many terms are locally
constant. A finite flat module over the Noetherian ring $A$ is finite
projective. For a flat constructible sheaf $F$, the successive open–closed
exact sequences express $F$ as a finite extension of the sheaves $a_!L$
attached to its strata, and the stupid filtration of the bounded flat complex
expresses $C$ as a finite extension of shifts of its *terms*. Each of these
operations preserves finite Tor amplitude. The same argument gives the
corresponding statement on $X_{\mathrm{ét}}$, which the compactness proof uses
before passing to the pro-étale site.

The lemma is phrased through flat models because the cohomology sheaves of
an object of $\Dctf$ need not have finite Tor amplitude. For example, the
complex $[A\xrightarrow{\ell}A]$ with $A=\mathbf Z/\ell^2\mathbf Z$ is perfect,
while its nonzero cohomology sheaves are copies of $\mathbf F_\ell$, which have
infinite projective dimension over $A$. Thus $\Dctf$ is a thick triangulated
category that is not the bounded derived category of an abelian category of
sheaves of finite Tor amplitude.
