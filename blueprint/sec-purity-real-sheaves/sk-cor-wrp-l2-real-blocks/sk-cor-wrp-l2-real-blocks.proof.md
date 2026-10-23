+++
kind  = "proof"
of    = "sk-cor-wrp-l2-real-blocks"
uses = ["det-wrp-real-weight-split"]
+++
Since semisimplification does not change traces, we may assume that
the sheaf is semisimple. By [sk-p-real-purity] it is then a
direct sum of pure summands of distinct weights. Each summand is real,
because at a fixed point eigenvalues of distinct weights have distinct
absolute values, and so complex conjugation, which preserves the whole
multiset, preserves the multiset of each summand
([det-wrp-real-weight-split]). By [sk-thm-wrp-l2-dictionary], the summand of
largest weight has growth parameter equal to its weight, and the other
summands have strictly smaller parameters. Applying the inequality
$|z+u|^2\le2|z|^2+2|u|^2$ in both directions, as in the proof of
[sk-lem-wrp-l2-growth], to the trace of the largest summand and the
sum of the other traces, we see that the other summands do not change
the parameter. This proves the first assertion.

For the second assertion, we apply the theorem on the open curve.
Extension by zero only adds zero traces. For $j_*$, the boundary
eigenvalues have weights at most $w$ by [sk-p-real-semi], so their finite
contribution has parameter at most $w-1$. Hence, by the last assertion of
[sk-lem-wrp-l2-growth], the parameter is still $w$.
