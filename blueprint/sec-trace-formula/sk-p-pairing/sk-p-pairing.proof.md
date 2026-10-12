+++
kind  = "proof"
of    = "sk-p-pairing"
+++
The supported-class bijection of [sk-d-corr], followed by [sk-thm-sf-kunneth-verdier],
turns $v$ at a point into
$(v\otimes1)\mathrm{coev}_P:A\to P\otimes P^\vee$.
For the diagonal identity, the contraction in [sk-d-pairing] reduces
by a triangle identity to symmetry followed by evaluation.
This is the composite of [sk-d-trace]; [sk-p-trace] fixes its signs.

The same adjunction calculation identifies the trace class of
[sk-d-trace-class] on any $X$. If $f:\Fix(c)\to X$, its exceptional adjoint is

$$
Rf_!A_{\Fix(c)}\simeq\Delta^*Rc_!A_C
\xrightarrow{\Delta^*\widetilde u}K\otimes D_XK
\xrightarrow{\mathrm{ev}\circ\mathrm{sym}}\omega_X.
$$

Indeed, under tensor–Hom adjunction and biduality from [sk-thm-sf-package],
the class of the diagonal identity maps to $1_K$. The supported cup
product reduces by the projection formula and $!$-base change in
[sk-d-six] to the displayed composite. This is the classical trace-class
dictionary used by the general proper-compatibility theorem below, on the specified fixed scheme.
