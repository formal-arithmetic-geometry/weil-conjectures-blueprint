+++
kind  = "proof"
of    = "det-prop-double-trace"
+++
Apply the Fourier trace formula [thm-fd-fourier-trace] twice, with $\psi$ and
then with $\psi^{-1}$; the orthogonality [lem-fd-additive-orthogonality] in
the form $\sum_y\psi_n((x-x')y)=q^n\delta_{x,x'}$ returns $q^nt_K(x)$. The
Tate twist $K(-1)$ has trace function $q^nt_K$ at degree-$n$ points by the
normalization built into the twist [def-wf-tate-twist].
