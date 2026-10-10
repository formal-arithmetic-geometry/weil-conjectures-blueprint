+++
kind  = "proof"
of    = "def-wf-lie-algebra-derivation"
+++
*The dual-number description of $T_xX$.* A $k$-algebra map
$A\to k[\varepsilon]/\varepsilon^2$ reducing to evaluation at $x$ has the
form $f\mapsto f(x)+\varepsilon\,v(f)$ with $v$ a $k$-derivation at $x$.
The Leibniz rule forces $v(\mathfrak m_x^2)=0$ and $v(1)=0$, so
$v|_{\mathfrak m_x}$ is a linear form killing $\mathfrak m_x^2$; conversely
every such form extends uniquely to a derivation at $x$ via
$A=k\oplus\mathfrak m_x$. The chain rule follows because the dual-number
description of the differential is composition with comorphisms.

*The Lie algebra and the adjoint action.* That
$\operatorname{Lie}(G)\subseteq\operatorname{End}(V)$ is closed under the
bracket, and that $dr$ preserves brackets, is standard (Milne,
*Algebraic Groups* (2017), Chapter 10). For the adjoint action, over
$k[\varepsilon]/\varepsilon^2$ one has
$(1+\varepsilon Y)X(1+\varepsilon Y)^{-1}=X+\varepsilon(YX-XY)$, so the
differential of $\operatorname{Ad}$ is $\operatorname{ad}(Y)X=[Y,X]$.
