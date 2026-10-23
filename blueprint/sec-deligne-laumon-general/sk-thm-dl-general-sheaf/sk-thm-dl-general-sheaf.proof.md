+++
kind  = "proof"
of    = "sk-thm-dl-general-sheaf"
+++
We first show that the asserted property is stable under composition.
For $X_0\xrightarrow{h}Z_0\xrightarrow{g}Y_0$, consider the Leray
spectral sequence for compact supports,

$$
 E_2^{a,b}=R^ag_!(R^bh_!F)\ \Longrightarrow\ R^{a+b}(gh)_!F.
$$

It is Frobenius-equivariant by the naturality of the truncation tower
and of the composition isomorphism for direct image with proper
support ([sk-thm-sf-comp-composition]). If both maps have the asserted
property, then $E_2^{a,b}$ has weights at most $w+a+b$. Each later
page is a subquotient, and the abutment filtration, which is finite
because the operations preserve bounded constructible complexes
([sk-thm-sf-ctf-stability]), has the same bound in each total degree.

Now apply [sk-l-dl-general-normalization], refining the
partitions to filtrations by open and closed pieces. On every refined
source piece, the first map is separated and quasi-finite, and so it
has the property by [sk-l-dl-general-quasifinite]; each projection of
a relative affine line has it by [sk-prop-wgen-relative-line].
By the composition argument, the map from the piece to $V$ has the
property. Gluing on the source and on the target, with the exact
sequence in each degree (the localization observation in the proof of
[sk-prop-wgen-relative-line]), we reassemble the finite partitions. Since restrictions of $F$ keep
its bound, this proves the assertion on $Y_0$.
