+++
id = "det-def-sfb-ring-object-transport"
kind = "lemma"
title = "Strong monoidal functors preserve ring objects"
lean = ["CategoryTheory.Functor.monObjObj", "CategoryTheory.Functor.map.instIsMonHom", "CategoryTheory.Functor.mapMon", "CategoryTheory.Functor.isCommMonObj_obj", "CategoryTheory.Functor.mapMonNatTrans"]
order = 1163
uses = ["det-def-sfb-ring-object-monoid"]
+++
Let $F\colon\mathcal C\to\mathcal D$ be a lax monoidal functor between monoidal categories, with
structure maps $\mu^F_{X,Y}\colon FX\otimes FY\to F(X\otimes Y)$, natural in $X,Y$, and
$\varepsilon^F\colon\mathbf 1\to F\mathbf 1$, satisfying the usual associativity and unit
coherences. (A strong monoidal functor is the case where these are isomorphisms.) For a ring object
$(R,\mu,\eta)$ of $\mathcal C$ ([det-def-sfb-ring-object-monoid]) put
$$
\mu_{FR}:=F(\mu)\circ\mu^F_{R,R}\colon FR\otimes FR\to FR,\qquad \eta_{FR}:=F(\eta)\circ\varepsilon^F\colon\mathbf 1\to FR .
$$
Then:

1. $(FR,\mu_{FR},\eta_{FR})$ is a ring object of $\mathcal D$, and for a morphism $f$ of ring
   objects, $Ff$ is a morphism of ring objects; this defines a functor
   $\mathrm{Mon}(F)\colon\mathrm{Mon}(\mathcal C)\to\mathrm{Mon}(\mathcal D)$ over $F$;
2. if $\mathcal C,\mathcal D$ are braided and $F$ is braided, i.e.
   $F(\beta_{X,Y})\circ\mu^F_{X,Y}=\mu^F_{Y,X}\circ\beta_{FX,FY}$, then $FR$ is commutative whenever
   $R$ is;
3. a monoidal natural transformation $\tau\colon F\Rightarrow F'$ between lax monoidal functors has
   components $\tau_R\colon FR\to F'R$ that are morphisms of ring objects; in particular a monoidal
   natural isomorphism gives isomorphic ring objects.
