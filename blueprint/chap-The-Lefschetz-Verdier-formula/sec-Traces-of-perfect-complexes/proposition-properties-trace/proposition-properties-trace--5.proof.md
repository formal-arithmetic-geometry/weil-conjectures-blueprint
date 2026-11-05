+++
kind = "proof"
of = "proposition-properties-trace--5"
order = 895012
uses = ["definition-categorical-trace"]
+++
The hypotheses on the unit make $K=\End(\mathbf 1)$ a field. Choose a
finite unit basis for each object. The functor
$\Hom(\mathbf 1,-)$ gives finite-dimensional spaces over $K^{\mathrm{op}}$;
on these finite free objects it takes the exact triples to exact
sequences, and the trace of an induced linear map is the opposite of
its categorical trace. These comparisons are
`CategoryTheory.MonoidalCategory.UnitBasis.exact_rightCompEndOp` and
`CategoryTheory.MonoidalCategory.UnitBasis.trace_rightCompEndOp`.

Reindex by $j=-n$ so that the connecting maps lower $n$ by one, and apply
`LinearMap.sum_negOnePow_smul_trace_sub_trace_sub_trace_eq_zero` on
the finite interval supplied by boundedness. The endomorphisms commute
with the induced linear maps. Replace the linear traces by categorical
traces, use $(-1)^{-n}=(-1)^n$, and rearrange. Terms outside the interval
vanish, giving the stated equality of alternating sums.
