+++
kind = "proof"
of = "det-def-sfb-filtered-two-colimit-characterization"
+++
1. The objects of $\mathcal D$ in the essential image of $\Phi$ are those isomorphic to some
   $\Phi(i,x)=\Phi_i(x)$, which is (Obj).
2. Every morphism $(i,x)\to(j,y)$ of $\mathcal C_\infty$ is a class $[k,g]$ with $k\ge i,j$ and
   $g\colon T_{ik}x\to T_{jk}y$, and $\Phi([k,g])=\theta_{jk,y}\Phi_k(g)\theta_{ik,x}^{-1}$. So the
   image of $\Hom_{\mathcal C_\infty}((i,x),(j,y))\to\Hom_{\mathcal D}(\Phi_ix,\Phi_jy)$ consists exactly
   of the morphisms of the form in (Hom-surj), and surjectivity for all $(i,x),(j,y)$ is (Hom-surj).
3. Suppose (Hom-inj), and let $[k,g],[k',g']\colon(i,x)\to(j,y)$ have the same image. Choose
   $m\ge k,k'$ and put $g_m=t_{km}(g)$, $g'_m=t_{k'm}(g')$, morphisms $T_{im}x\to T_{jm}y$ of
   $\mathcal C_m$. By well-definedness of $\Phi$, $\theta_{jm,y}\Phi_m(g_m)\theta_{im,x}^{-1}=\theta_{jm,y}\Phi_m(g'_m)\theta_{im,x}^{-1}$,
   so $\Phi_m(g_m)=\Phi_m(g'_m)$. By (Hom-inj) there is $m'\ge m$ with $T_{mm'}(g_m)=T_{mm'}(g'_m)$,
   hence $t_{mm'}(g_m)=t_{mm'}(g'_m)$ and $[k,g]=[k',g']$. So $\Phi$ is faithful.

   Conversely, suppose $\Phi$ faithful, and let $g,g'\colon x\to y$ in $\mathcal C_k$ with
   $\Phi_k(g)=\Phi_k(g')$. Since $T_{kk}=\mathrm{Id}$ and $\theta_{kk}=\mathrm{id}$, $[k,g]$ and $[k,g']$ are
   morphisms $(k,x)\to(k,y)$ with $\Phi([k,g])=\Phi_k(g)=\Phi_k(g')=\Phi([k,g'])$. So $[k,g]=[k,g']$:
   there is $k'\ge k$ with $t_{kk'}(g)=t_{kk'}(g')$, i.e.
   $\tau_{kkk',y}T_{kk'}(g)\tau_{kkk',x}^{-1}=\tau_{kkk',y}T_{kk'}(g')\tau_{kkk',x}^{-1}$; as
   $\tau_{kkk'}$ is the identity, $T_{kk'}(g)=T_{kk'}(g')$. This is (Hom-inj).

Finally, a functor is an equivalence if and only if it is fully faithful and essentially surjective.
