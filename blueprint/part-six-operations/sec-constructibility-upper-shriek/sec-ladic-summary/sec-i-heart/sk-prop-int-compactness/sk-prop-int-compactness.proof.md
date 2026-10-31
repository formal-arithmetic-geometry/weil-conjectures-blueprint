+++
kind = "proof"
of = "sk-prop-int-compactness"
uses = ["sk-thm-constructible-compactness", "sk-lem-finite-window", "sk-lem-proper-unbounded-window", "sk-lem-int-integral-heart", "sk-lem-formal-closed-support", "sk-cor-pe-bounded-continuity", "sk-def-cd"]
+++
The rational proofs (Theorem [sk-thm-constructible-compactness],
Lemmas [sk-lem-finite-window] and [sk-lem-proper-unbounded-window])
use Lemma [sk-lem-int-integral-heart](1), continuity of $\Ext^i(C,-)$ for
bounded below systems, a bound $d_C$ with $\Ext^i(C,N)=0$ for $i>d_C$ and
$N$ constructible, and a bound on the amplitude of $Rp_*$. For $C=a_!L$ on a
stratum, $R\!\operatorname{Hom}(a_!L,-)$ is $R\Gamma(S,-)$ of the dual of $L$ tensored with
$u^*R\underline\Gamma_Z$ (Lemma [sk-lem-formal-closed-support](2); its
proof uses only that $L$ is dualizable, Lemma [sk-lem-int-integral-heart](3)), so
continuity follows from Corollary [sk-cor-pe-bounded-continuity]. The bound
follows by counting degrees: the reductions of $N$ lie in $[-1,0]$, the dual
adds one, $R\Gamma$ and $R\underline\Gamma_Z$ add the dimensions of
Definition [sk-def-cd], and $R\varprojlim$ adds one [Stacks, Tag 08TB](https://stacks.math.columbia.edu/tag/08TB);
likewise $Rp_*$ of a constructible sheaf lies in $[0,2d+1]$ for fibres of
dimension $\le d$ [Stacks, Tag 095U](https://stacks.math.columbia.edu/tag/095U).
