+++
kind  = "proof"
of    = "thm-sf-preservation-class"
+++
*Step 1: which functor is bounded.* By
[def-weil-exceptional-inverse-image] the functor $Rf^!$ is, on the
bounded constructible category $D^b_c(Y,A_{E,n})$, the restriction of the
ambient right adjoint $Rf_n^{\times}$ of $Rf_{!,n}$, and its restriction
to finite-Tor objects is the corresponding restriction of the same functor.
On the blueprint's coefficient class [def-sf-fullcd-used-class] that
right adjoint exists and is the explicit composite
$\nu_X^*f^{\times}R\nu_{Y,*}$ of
[thm-sf-ambient-adjoint-class](2), which also supplies its unit, its
counit and the compactification comparisons; the comparison morphisms
$\nu_X,\nu_Y$ are those of
[def-weil-pbc-site-comparison-morphism]. That the bounded constructible
and finite-Tor objects are exactly the complexes coming from the étale site
is [lem-sf-proetale-constructible-origin], and that both halves of the
ambient datum are theorems on that class is
[cor-sf-ambient-adjoint-discharge]. The bounds proved below are
therefore bounds on that explicitly constructed functor, and no clause of
[def-weil-ambient-exceptional-adjoint] is used in stating them.

*Step 2: the two bounds are the assembly of the purity chapter.* The
setting of [def-pur-conventions] is the present one: the same global
finite-field datum, the same $k=\Fbar$, the same separated finite-type
morphism $f:X\to Y$ between finite-type $k$-schemes and the same
coefficient ring $A=A_{E,n}$. [thm-pur-general-admissibility] proves
that a separated finite-type morphism satisfies the two preservation clauses
of [def-weil-exceptional-adjoint-admissibility] as soon as the
open-complement condition of [def-exc-open-complement-bound] holds for
the finitely many pairs $(W_U,\mathbf A^{d_U}_V)$ formed by the affine
charts of the statement, $W_U$ being the complement of $U$ in the affine
space $\mathbf A^{d_U}_V$ of [def-sbc-affine-space]; and
[cor-pur-general-admissibility-datum] removes that hypothesis by
[lem-exc-open-complement-known]. Indeed $\mathbf A^{d_U}_V$ is of
finite type over $k$ of dimension $d_U+\dim V\leq d_U+\dim Y$, the
complement $W_U$ is a quasi-compact open subscheme of it, and $A=A_{E,n}$
is a finite ring annihilated by the power $\pi_E^n$ of the prime
$\ell\neq\operatorname{char}(k)$, so the pair satisfies the
open-complement condition with $c_U=2(d_U+\dim Y)$. The conclusion of
[cor-pur-general-admissibility-datum] is, in the notation of
[def-weil-constructible-intervals] and
[def-weil-finite-tor-amplitude], that $Rf^!$ carries
$D_c^{[a,b]}(Y,A)$ into $D_c^{[a-2D,b-2D+c]}(X,A)$ and finite Tor
amplitude in $[a,b]$ to finite Tor amplitude in $[a-2D,b-2D+c]$, where
$D=\max_Ud_U$ and $c=\max_U(c_U+1+2(D-d_U))$. For every chart $U$,

$$
c_U+1+2(D-d_U)=2d_U+2\dim Y+1+2D-2d_U=2D+2\dim Y+1,
$$

so the maximum is $c=2D+2\dim Y+1$, the lower end is $a-2D$, and the two
bounds become $[a-2D,b+2\dim Y+1]$: these are clauses (1) and (2) of the
statement. No clause of [def-weil-exceptional-adjoint-admissibility] is
used: [cor-pur-general-admissibility-datum] displays the ambient datum
only to record that on the coefficients it quantifies over — the bounded
constructible and finite-Tor objects, of étale origin by
[lem-sf-proetale-constructible-origin] — that datum is the theorem
[cor-sf-ambient-adjoint-discharge], whose vanishing half is the
class-restricted datum [def-sf-fullcd-class] supplied by
[thm-sf-fullcd-class] with the sharp comparison bound $M=0$ of
[prop-sf-comparison-bound-zero].

*Step 3: independence of the admissible coefficient ring.* The charts
$U\subseteq f^{-1}(V)$, the integers $d_U$ and the number
$\dim V\leq\dim Y$ come from the presentation of the coordinate rings
$\mathcal O(U)$ over $\mathcal O(V)$, an operation on the schemes alone,
and do not depend on the coefficient ring; and the hypotheses under which
[lem-exc-open-complement-known] was applied in Step 2 are the same at
every finite stage, $A_{E,n}$ being a finite ring annihilated by the power
$\pi_E^n$ of $\ell$. Hence both the open-complement condition with
the constants $c_U$ and the constants $D$, $c$ of
[thm-pur-general-admissibility] and
[cor-pur-general-admissibility-datum] are the same integers at every
stage, and instantiating that corollary at each $n\geq1$ gives clauses (1)
and (2) at $A_{E,n}$ with these constants and with no hypothesis; this is
clause (3). It is the stage-uniform form of the open-complement condition
recorded in [thm-pur-open-complement-unconditional].

*Step 4: reading the bounds in the definitions.* Clause (2) of
[def-weil-exceptional-adjoint-admissibility] asks for signed integers
$c_f^-,c_f^+\in\mathbf Z$ with
$Rf_n^{\times}L\in D_c^{[a+c_f^-,b+c_f^+]}(X,A)$ for every
$L\in D_c^{[a,b]}(Y,A)$, and clause (3) asks that $Rf_n^{\times}$ carry
$D^b_{ctf}(Y,A)$ into $D^b_{ctf}(X,A)$; by clauses (1) and (2) these hold
with $c_f^-=-2D$ and $c_f^+=2\dim Y+1$, and by Step 1 the functor these
two clauses bound is $Rf^!$ on the two categories they concern. Clause (1)
of the same definition is not assumed: the existence of $Rf_n^{\times}$ on
those categories, with its unit, counit and compactification comparisons, is
Step 1, that is [thm-sf-ambient-adjoint-class] read through
[def-weil-exceptional-inverse-image] and
[cor-sf-ambient-adjoint-discharge]. Finally clause (v) of
the finite-Tor preservation summary is the same two assertions at the coefficient
stage $\Lambda=A$, with the membership
$Rf^!D^b_{ctf}(Y,A)\subseteq D^b_{ctf}(X,A)$ as its conclusion and the
ambient exceptional right adjoint datum as its displayed hypothesis; by
Step 1 that hypothesis is, on that category and at that stage, the theorem
[cor-sf-ambient-adjoint-discharge], so the clause holds for every
separated finite-type morphism $f$ without it. The assertions of the
statement for the remaining admissible coefficient rings are exactly the assertions
that this proof does not make, as the last paragraph of the statement
records.
