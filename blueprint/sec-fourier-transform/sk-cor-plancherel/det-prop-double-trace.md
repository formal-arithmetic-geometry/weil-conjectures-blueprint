+++
id = "det-prop-double-trace"
kind = "corollary"
title = "Trace-level Fourier inversion"
lean = ["AlgebraicGeometry.WeilComplex.traceFunction_fourierTransform_inv_fourierTransform", "FiniteField.fourierTransform_inv_fourierTransform"]
order = 3970
uses = ["lem-fd-additive-orthogonality", "thm-fd-fourier-trace", "def-wf-tate-twist"]
+++
For a constructible Weil complex $K$ on $\Aone$, every $n\ge1$ and every
$y\in\mathbf F_{q^n}$,

$$
t_{\FT_{\psi^{-1}}\FT_\psi(K)}(y)=q^n\,t_K(y),
$$

which is the trace function of the Tate twist $K(-1)$ at points of degree
$n$.
