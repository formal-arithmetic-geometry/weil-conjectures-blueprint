+++
id = "prose-01-07"
kind = "hidden"
title = "What these notes contain"
order = 15
+++
The main theorem of these notes is the Weil conjectures for smooth
proper varieties over $\mathbf F_q$ (Theorem [sk-thm-weil-final]),
with the statement on Betti numbers in the form explained above. The
proof follows Weil's plan: we construct the cohomology, prove the axioms
(a)–(c) for it, and then prove purity (d). Each part uses the one
before it.

Part “The six operations” constructs the six operations on
$D^b_{\mathrm{ctf}}(X,\Lambda)$ for all admissible coefficient rings at once
(Theorem [sk-thm-existence]). The new operation is $f^!$: Brown
representability gives it as a right adjoint of $Rf_!$, and the
geometric content of the theorem is that $f^!$ preserves
constructibility. Part “Duality and the trace formula” makes these functors compute
something. Its first main result is smooth purity
(Theorem [sk-thm-purity-transport]): for $f$ smooth of relative dimension
$d$ we have $f^!\simeq f^*(d)[2d]$. This identifies the dualizing complex
of a smooth variety, so that Verdier duality becomes Poincaré duality
between $H^i_c$ and $H^{2d-i}(d)$ (Theorem [sk-thm-sf-global-duality]). The
same isomorphism provides the trace map and the class of the diagonal,
and from them we obtain the Grothendieck–Lefschetz trace formula for
every Weil complex (Theorem [sk-thm-tf-uniform-formula]). Rationality and
the functional equation follow. Part “Weights and the Riemann hypothesis” proves Deligne's
theorem that $Rf_!$ does not increase weights
(Theorem [sk-cor-dl-general-complex]). There the trace formula is
used in the other direction: it writes the $L$-function of a sheaf on a
curve in terms of cohomology, and positivity of the coefficients of the
Euler product then
bounds the Frobenius eigenvalues. Applied to the constant sheaf on a
smooth proper $X_0$, the theorem bounds the eigenvalues on $H^i$ by
$q^{i/2}$ from above. Poincaré duality from Part “Duality and the trace formula”
pairs $\alpha$ with $q^d/\alpha$ and gives the bound from below, which
is purity, and the Weil conjectures follow
(Theorem [sk-thm-weil-final]).

In more detail, the parts are as follows.

- Part “The six operations” (Sections [sec-proetale-coefficients]–[sec-smooth-base-change])
  constructs the six operations for all coefficient rings
  (Theorem [sk-thm-existence]). It ends with smooth base change, which
  enters the ordinary Künneth formula used in Part “Duality and the trace formula”.
- Part “Duality and the trace formula” (Sections [sec-smooth-purity]–[sec-trace-formula])
  proves smooth purity $f^!\simeq f^*(d)[2d]$, Verdier and Poincaré
  duality, which is (c), and the trace formula (b) with its Frobenius
  compatibilities, and it ends with rationality and the functional
  equation. As for (a), the groups $H^i_c$ are finite because $Rf_!$
  preserves $D^b_{\mathrm{ctf}}$ (Part “The six operations”), and they vanish outside
  $[0,2\dim X]$ for smooth proper $X$ (Theorem [sk-cor-trace]).
- Part “Weights and the Riemann hypothesis” (Sections [sec-weights-deligne-theorem]–[sec-zeta-weil])
  proves purity (d) and the Weil conjectures, following (WBP).
  Section [sec-weights-deligne-theorem] explains how the argument is organized.

The appendices prove results from algebraic geometry that we use.
