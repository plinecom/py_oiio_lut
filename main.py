import OpenImageIO as oiio
import glob

if __name__ == '__main__':

    for path in glob.glob('/foo/bar/*.exr'):
        print(path)
        jpg_path = path.replace('.exr', '_lut.jpg')

        #Read File
        buf = oiio.ImageBuf(path)

        #Apply Lut File
        dst = oiio.ImageBuf()
        isOK = oiio.ImageBufAlgo.ociofiletransform(dst, buf,
                                                  "/foo/bar/test.cube",
                                                  False)
        if not isOK:
            print("ociofiletransform error: " + dst.geterror())
            continue

        #Write File
        dst.write(jpg_path)
