+++
kind = "proof"
of = "sk-cor-pe-bounded-continuity"
uses = ["sk-prop-pe-hypercover", "sk-cor-pe-sections"]
+++
Use the same hypercover $W_\bullet$ for all $i$ ([sk-prop-pe-hypercover]). By
[sk-cor-pe-sections], sections on each $W_r$ commute with filtered colimits, and therefore so
does the finite sum in each total degree of the hypercover complex. Since filtered colimits of
modules are exact, the first assertion follows. For direct images, evaluate the cohomology
presheaves on affine objects $V$ of $Y_{\mathrm{proét}}$. Each $X\times_YV$ is quasi-compact
and quasi-separated, so that the first assertion applies, and sheafification commutes with
colimits ([det-pe-bounded-continuity-direct-image]).
