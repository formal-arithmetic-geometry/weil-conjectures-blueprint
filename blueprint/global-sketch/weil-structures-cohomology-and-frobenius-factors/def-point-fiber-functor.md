+++
id = "def-point-fiber-functor"
kind = "definition"
title = "Derived fiber over the geometric point"
order = 87
uses = ["def-point-coefficient-categories", "def-weil-base-field", "def-weil-finite-coefficient-datum"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum], put
$s=\Spec k$, and let $\bar s\to s$ be its geometric point. For
$\Lambda\in\{\mathcal O_E/\varpi_E^n,\mathcal O_E,E,\Qlb\}$, with
$n\geq1$ in the finite case, define the derived-stalk functor

$$
\operatorname{Fib}_{s,\Lambda}:D^b_c(s,\Lambda)\longrightarrow
\begin{cases}
D^b_{\mathrm{fin}}(\mathcal O_E/\varpi_E^n),
&\Lambda=\mathcal O_E/\varpi_E^n,\\
D^b_{\mathrm{fg}}(\mathcal O_E),&\Lambda=\mathcal O_E,\\
D^b_{\mathrm{fd}}(E),&\Lambda=E,\\
D^b_{\mathrm{fd}}(\Qlb),&\Lambda=\Qlb,
\end{cases}
\qquad K\longmapsto K_{\bar s}.
$$

The $\Qlb$-valued component is the common-stage form of the finite-stage
stalk equivalences and, under the defining identification
$D^b_{\mathrm{fd}}(\Qlb)=D^b_c(s,\Qlb)$, is the corresponding point
identification.
