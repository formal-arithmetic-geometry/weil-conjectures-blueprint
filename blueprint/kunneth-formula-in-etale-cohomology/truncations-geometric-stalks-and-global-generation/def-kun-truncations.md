+++
id = "def-kun-truncations"
kind = "definition"
title = "Truncations and homotopy colimits"
order = 6032
lean = ["CategoryTheory.Triangulated.hocolim"]
uses = ["def-weil-pbc-hypercohomology-filtrations", "lem-kun-stalks-commute-colimits"]
+++
For a complex $\mathcal E^\bullet$ of étale sheaves, the *stupid
truncations* $\sigma_{\ge n}$ and $\sigma_{\le n}$ are obtained by replacing
the terms in degrees $<n$ (resp. $>n$) by $0$. The *good (canonical)
truncations* $\tau_{\ge n}$, $\tau_{\le n}$ are the truncation functors of
the standard t-structure on $D(T_{\Et})$: they keep the cohomology objects
in the retained range and kill those outside it. The triangle
$$
\tau_{\le n-1}K\to\tau_{\le n}K\to\mathcal H^n(K)[-n]\to
$$
is the truncation couple of the spectral-sequence chapter; these truncation
triangles are the ones used for its hypercohomology filtrations.

In a triangulated category with countable direct sums, the *homotopy
colimit* of a sequence $E_0\to E_1\to\cdots$ is specified by a
distinguished triangle
$$
\bigoplus_nE_n\xrightarrow{\,1-\mathrm{shift}\,}\bigoplus_nE_n
\longrightarrow\operatorname{hocolim}_nE_n\longrightarrow\bigl(\bigoplus_nE_n\bigr)[1].
$$

The colimit of étale sheaves is the sheafification of the objectwise colimit
of the underlying presheaves. Geometric stalks are computed by filtered
colimits of sections over pointed étale neighbourhoods; their commutation
with colimits of sheaves, hence with colimits of complexes of sheaves, is
[lem-kun-stalks-commute-colimits].

Unresolved dependencies: def:sp-truncation-couple, def:weil-pbc-geometric-stalks
