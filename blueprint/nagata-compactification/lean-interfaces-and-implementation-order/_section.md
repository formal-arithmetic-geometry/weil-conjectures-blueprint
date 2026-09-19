+++
id = "lean-interfaces-and-implementation-order"
kind = "section"
title = "Lean interfaces and implementation order"
order = 551
+++
The basic bundled structure should expose all construction data rather than
only a proposition.

```
structure Compactification {X S : Scheme} (f : X -> S) where
  Xbar : Scheme
  j : X -> Xbar
  p : Xbar -> S
  fac : j >> p = f
  isOpenImmersion_j : IsOpenImmersion j
  quasiCompact_j : QuasiCompact j
  isProper_p : IsProper p

def Compactifiable {X S : Scheme} (f : X -> S) : Prop :=
  Nonempty (Compactification f)
```

The implementation order forced by the dependency graph is:

1. compactifications, scheme-theoretic images, restriction to opens, and
closed-subscheme inheritance;
1. admissible blow-ups, strict transforms, extension of centers, and
domination by product ideals;
1. boundary separation and elimination of indeterminacy;
1. common modifications, graph extension, and separated gluing;
1. the dense-source valuative criterion and the two-open theorem;
1. affine compactification and the Noetherian theorem;
1. finite-presentation reduction, Noetherian approximation, and the final
assembly.

Before any declaration receives a `\leanok` marker, the following points
must be checked in Lean:

1. every displayed composite equality is stated using the actual chosen
pullback and gluing morphisms;
1. every scheme-theoretic image is formed under the required
quasi-compactness hypotheses;
1. restriction of a scheme-theoretic image to an open target is available
as an equality or a specified isomorphism of closed subschemes;
1. every admissible blow-up carries a chosen lift and chosen isomorphism
over the preserved open;
1. the boundary-separation blow-ups preserve $V_i$, not only $U_i$;
1. the common-modification proof uses properness of
$X'_{12}\to X_1\times_SX_2$ and separatedness of the new product over the
old product; it does not incorrectly assume the projections
$X_{12}\to X_i$ are proper in the general common-modification lemma;
1. the dense-source valuative criterion is invoked with uniqueness, not
with existence alone;
1. the pair of valuation extensions factors scheme-theoretically through
$X_{12}$ by injectivity of $A\hookrightarrow K$;
1. the finite affine cover has dense total intersection, and the induction
uses density of each partial overlap;
1. finite presentation, the base-change identification, and separatedness
all descend at one common sufficiently large index.
