+++
kind = "proof"
of = "sk-lem-sf-flat-model"
uses = ["sk-cor-pe-finite-tor-comparison"]
+++
By Corollary [sk-cor-pe-finite-tor-comparison], $C=\nu_X^*C_{\acute{e}t}$ with
$C_{\acute{e}t}\in D^b_{\mathrm{ctf}}(X_{\acute{e}t},A)$, where
$\nu_X^*:D(X_{\acute{e}t},A)\to D(X_{\mathrm{pro}\acute{e}t},A)$ is the comparison inverse
image. The complex $C_{\acute{e}t}$ has a bounded flat model by [Stacks, Tag 0F4M](https://stacks.math.columbia.edu/tag/0F4M).
Since $\nu_X^*$ is exact on sheaves, it pulls this model back to a bounded flat
constructible model on $X_{\mathrm{pro}\acute{e}t}$. We choose a common stratification on
which its finitely many terms are locally constant. Recall that a finite flat
module over the Noetherian ring $A$ is finite projective. If $F$ is a flat
constructible sheaf, then the exact sequences for the successive open and closed
strata express $F$ as a finite extension of the sheaves $a_!L$ attached to its
strata. Similarly, the stupid filtration of the bounded flat complex expresses
$C$ as a finite extension of shifts of its *terms*. Both of these
operations preserve finite Tor amplitude. The same argument proves the
corresponding statement on $X_{\acute{e}t}$, which we use in the proof of
compactness below before passing to the pro-étale site.
