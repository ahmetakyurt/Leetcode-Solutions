class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Her zaman daha kısa olan dizi üzerinde binary search yapalım (Verimlilik için)
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2
        
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            # i: A dizisindeki kesim noktası (index)
            # j: B dizisindeki kesim noktası
            i = (l + r) // 2 
            j = half - i - 2 # -2 çünkü indeksler 0'dan başlıyor
            
            # Kenar durumları (Sınırları aşarsak eksi/artı sonsuz varsayıyoruz)
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            # Doğru kesim noktasını bulduk mu?
            if Aleft <= Bright and Bleft <= Aright:
                # Toplam eleman sayısı tek ise
                if total % 2:
                    return min(Aright, Bright)
                # Toplam eleman sayısı çift ise
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            # Kesim noktasını kaydır
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1