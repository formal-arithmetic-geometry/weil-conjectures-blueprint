+++
kind  = "proof"
of    = "thm-fd-fourier-trace"
+++
By [lem-fd-stalk-formula], the stalk of $\operatorname{FT}_\psi(K)$ at the geometric point over $y$ is the shifted compact-support complex $H^*_c(\mathbf A^1,K\otimes^L\mathcal L_{\psi(xy)})[1]$. The Grothendieck–Lefschetz trace formula over $\mathbf F_{q^n}$,
[thm-trf-grothendieck-lefschetz-qbar] (in the point-counting form of [cor-trf-point-counting]), computes the trace of the Frobenius on that complex as the sum of the traces on the geometric points of the fibre, i.e. $-\sum_{x\in\mathbf F_{q^n}}t_{K\otimes^L\mathcal L_{\psi(xy)}}(x)$: the sign is the shift $[1]$ of [def-fd-transform]. The trace of the tensor product is the product of the traces, and the trace of the Artin–Schreier summand at $x$ is $\psi(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(xy))$ by [lem-fd-as-trace]; this gives the displayed formula.
